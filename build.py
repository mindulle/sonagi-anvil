import os
import json
import re

CONTENT_DIR = "content"
OUTPUT_FILE = "public/questions.js"

def parse_markdown(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 정규식으로 섹션 파싱
    prompt_match = re.search(r'# Prompt\n(.*?)\n# Buggy Code', content, re.DOTALL)
    code_match = re.search(r'# Buggy Code\n```python\n(.*?)\n```\n# Solution', content, re.DOTALL)
    solution_match = re.search(r'# Solution\n(.*?)$', content, re.DOTALL)

    if not (prompt_match and code_match and solution_match):
        print(f"Skipping {filepath}: Invalid format")
        return None

    return {
        "id": os.path.basename(filepath).replace('.md', ''),
        "prompt": prompt_match.group(1).strip(),
        "code": code_match.group(1).strip(),
        "solution_html": markdown_to_html(solution_match.group(1).strip())
    }

def markdown_to_html(text):
    # 매우 단순한 마크다운 -> HTML 변환 (실제로는 markdown 라이브러리 권장)
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
    text = re.sub(r'### (.*?)\n', r'<h3>\1</h3>\n', text)
    text = text.replace('\n', '<br>')
    return text

def main():
    questions = []
    if not os.path.exists(CONTENT_DIR):
        os.makedirs(CONTENT_DIR)
        
    for filename in os.listdir(CONTENT_DIR):
        if filename.endswith(".md"):
            q = parse_markdown(os.path.join(CONTENT_DIR, filename))
            if q:
                questions.append(q)

    # JS 변수로 저장 (프론트엔드에서 바로 로드 가능하게)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(f"const ASSESSMENT_QUESTIONS = {json.dumps(questions, ensure_ascii=False, indent=2)};")
    print(f"Built {len(questions)} questions into {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
