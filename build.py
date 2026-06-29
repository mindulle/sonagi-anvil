import os
import json
import re

CONTENT_DIR = "content"
OUTPUT_DIR = "public"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "questions.js")

def parse_markdown(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    prompt = ""
    code = ""
    solution = ""

    if "# Prompt" in content and "# Buggy Code" in content:
        prompt = content.split("# Prompt")[1].split("# Buggy Code")[0].strip()
    
    if "# Buggy Code" in content and "# Solution" in content:
        code_section = content.split("# Buggy Code")[1].split("# Solution")[0].strip()
        code_match = re.search(r'```(?:python|javascript)?\n(.*?)\n```', code_section, re.DOTALL)
        code = code_match.group(1) if code_match else code_section
        
    if "# Solution" in content:
        solution = content.split("# Solution")[1].strip()

    if not prompt or not code or not solution:
        return None

    return {
        "id": os.path.basename(filepath).replace('.md', ''),
        "prompt": prompt,
        "code": code,
        "solution_html": markdown_to_html(solution)
    }

def markdown_to_html(text):
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
    text = re.sub(r'### (.*?)\n', r'<h3>\1</h3>\n', text)
    text = text.replace('\n', '<br>')
    return text

def main():
    questions = []
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    # src 폴더의 정적 파일들을 public으로 복사
    os.system(f"cp src/index.html {OUTPUT_DIR}/ 2>/dev/null")
        
    for filename in os.listdir(CONTENT_DIR):
        if filename.endswith(".md"):
            q = parse_markdown(os.path.join(CONTENT_DIR, filename))
            if q:
                questions.append(q)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(f"const ASSESSMENT_QUESTIONS = {json.dumps(questions, ensure_ascii=False, indent=2)};")
    print(f"Built {len(questions)} questions into {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
