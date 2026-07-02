#!/usr/bin/env python3
import sys
import os
import time
import json
import sqlite3
import subprocess
import urllib.request
import urllib.parse
from datetime import datetime, timezone

DB_PATH = "metrics.db"
STATE_FILE = ".training_state.json"
DEFAULT_WEBHOOK_URL = "http://100.113.113.72/webhook/anvil-metrics"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS submissions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  problem_name TEXT,
                  categories TEXT,
                  difficulty TEXT,
                  time_taken_seconds INTEGER,
                  passed BOOLEAN,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    return conn

def start(problem_name):
    if not os.path.isdir(problem_name):
        print(f"❌ 오류: 문제 폴더 '{problem_name}' 가 존재하지 않습니다.")
        sys.exit(1)
    
    state = {"problem_name": problem_name, "start_time": time.time()}
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)
        
    print(f"⏱️  타이머가 시작되었습니다: '{problem_name}'")
    print("문제를 다 푼 후에는 `./train.py submit` 명령어를 실행하여 채점하세요!")

def submit():
    if not os.path.exists(STATE_FILE):
        print("❌ 진행 중인 훈련이 없습니다. `./train.py start <폴더명>`을 먼저 실행하세요.")
        sys.exit(1)
        
    with open(STATE_FILE, "r") as f:
        state = json.load(f)
    
    problem_name = state["problem_name"]
    time_taken = int(time.time() - state["start_time"])
    
    print(f"🧪 '{problem_name}' 테스트 코드를 실행합니다...\n")
    
    # Run pytest
    result = subprocess.run(["pytest", f"{problem_name}/"], capture_output=True, text=True)
    passed = result.returncode == 0
    
    # Load metadata
    meta_path = os.path.join(problem_name, "meta.json")
    categories = "Unknown"
    difficulty = "Unknown"
    if os.path.exists(meta_path):
        with open(meta_path, "r") as mf:
            meta = json.load(mf)
            categories = ",".join(meta.get("categories", []))
            difficulty = meta.get("difficulty", "Unknown")
            
    # Save to DB
    conn = init_db()
    c = conn.cursor()
    c.execute("INSERT INTO submissions (problem_name, categories, difficulty, time_taken_seconds, passed) VALUES (?, ?, ?, ?, ?)",
              (problem_name, categories, difficulty, time_taken, passed))
    conn.commit()
    
    # Send to n8n Webhook
    webhook_url = os.environ.get("ANVIL_METRICS_WEBHOOK_URL", DEFAULT_WEBHOOK_URL)
    try:
        payload = {
            "id": f"sub_{int(time.time())}",
            "problemId": problem_name,
            "categories": categories,
            "difficulty": difficulty,
            "timeTakenSeconds": time_taken,
            "isPassed": passed,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
        req = urllib.request.Request(webhook_url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
        urllib.request.urlopen(req, timeout=3)
        print("🌐 n8n Webhook 연동 성공 (데이터 전송 완료)")
    except Exception as e:
        print(f"⚠️ n8n Webhook 연동 실패 (로컬 DB에만 저장되었습니다): {e}")

    # Clear state
    os.remove(STATE_FILE)
    
    minutes, seconds = divmod(time_taken, 60)
    print(f"✅ 제출 완료! (소요 시간: {minutes}분 {seconds}초)")
    
    if passed:
        print("\n🎉 모든 테스트 케이스를 통과했습니다! (PASS)")
    else:
        print("\n❌ 일부 테스트 케이스에서 실패했습니다. (FAIL)\n")
        print(result.stdout)

def stats():
    conn = init_db()
    c = conn.cursor()
    c.execute("SELECT COUNT(*), SUM(CASE WHEN passed THEN 1 ELSE 0 END), AVG(time_taken_seconds) FROM submissions")
    row = c.fetchone()
    
    total = row[0]
    if total == 0:
        print("📊 아직 누적된 훈련 데이터가 없습니다.")
        return
        
    passed = row[1] or 0
    avg_time = int(row[2] or 0)
    
    print("\n📊 --- 전체 훈련 통계 --- 📊")
    print(f"총 제출 횟수   : {total} 회")
    print(f"정답률(Pass)  : {passed}/{total} ({int(passed/total*100)}%)")
    print(f"평균 소요 시간 : {avg_time//60}분 {avg_time%60}초\n")
    
    print("🔍 [카테고리별 상세 통계]")
    c.execute("""
        SELECT categories, COUNT(*), SUM(CASE WHEN passed THEN 1 ELSE 0 END), AVG(time_taken_seconds) 
        FROM submissions GROUP BY categories
    """)
    for cat, count, p, t in c.fetchall():
        pr = int(p/count*100) if count > 0 else 0
        avg_t = int(t)
        print(f" - {cat}: 정답률 {pr}% (평균 {avg_t//60}분 {avg_t%60}초)")
        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: ./train.py [start <폴더명> | submit | stats]")
        sys.exit(1)
        
    cmd = sys.argv[1]
    if cmd == "start" and len(sys.argv) == 3:
        start(sys.argv[2])
    elif cmd == "submit":
        submit()
    elif cmd == "stats":
        stats()
    else:
        print("❌ 잘못된 명령어입니다.")
