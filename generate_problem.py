#!/usr/bin/env python3
import os
import sys
import json
import urllib.request
import re

def generate_problem(problem_name: str, api_key: str):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    
    prompt = f"""
You are an expert Data Structures and Algorithms instructor. 
Generate a Python skeleton and a pytest file for the problem: "{problem_name}".

The output MUST be in the following strict JSON format, without any markdown formatting around it:
{{
  "folder_name": "snake_case_problem_name",
  "file_name": "snake_case_problem_name.py",
  "skeleton_code": "class Solution:\n    def ...",
  "test_code": "import pytest\nfrom snake_case_problem_name import Solution\n..."
}}

Requirements:
1. skeleton_code: Contains the class/method definition and a docstring, with `# TODO: Implement` and `pass`.
2. test_code: Uses pytest. MUST include extreme edge cases: Empty inputs, single element, duplicates, and extreme limits.
"""

    data = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "response_mime_type": "application/json",
            "temperature": 0.2
        }
    }
    
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers={'Content-Type': 'application/json'})
    
    try:
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode('utf-8'))
        content = result['candidates'][0]['content']['parts'][0]['text']
        
        # Clean markdown if present
        if content.startswith('```json'):
            content = content.split('\n', 1)[1].rsplit('\n', 1)[0]
        elif content.startswith('```'):
            content = content.split('\n', 1)[1].rsplit('\n', 1)[0]
            
        return json.loads(content)
    except Exception as e:
        print(f"Error during API call: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_problem.py \"Problem Name or URL\"")
        sys.exit(1)
        
    problem_name = sys.argv[1]
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("❌ Error: GEMINI_API_KEY environment variable is not set.")
        print("Please run: export GEMINI_API_KEY='your_api_key'")
        sys.exit(1)
        
    print(f"🤖 Generating DSA problem '{problem_name}' via Gemini API...")
    
    data = generate_problem(problem_name, api_key)
    
    # Setup Directories
    base_dir = "dsa_training"
    os.makedirs(base_dir, exist_ok=True)
    
    # Find next problem number
    existing_dirs = [d for d in os.listdir(base_dir) if re.match(r'\d{2}_', d) and os.path.isdir(os.path.join(base_dir, d))]
    next_num = len(existing_dirs) + 1
    
    # Ensure sequential folder name
    folder_name = data['folder_name']
    folder_name = f"{next_num:02d}_{folder_name.split('_', 1)[-1]}" if re.match(r'\d{2}_', folder_name) else f"{next_num:02d}_{folder_name}"
    
    target_dir = os.path.join(base_dir, folder_name)
    template_dir = os.path.join(base_dir, ".templates", folder_name)
    
    os.makedirs(target_dir, exist_ok=True)
    os.makedirs(template_dir, exist_ok=True)
    
    # Write Files
    py_path = os.path.join(target_dir, data['file_name'])
    test_path = os.path.join(target_dir, f"test_{data['file_name']}")
    
    with open(py_path, "w") as f:
        f.write(data['skeleton_code'])
        
    with open(test_path, "w") as f:
        f.write(data['test_code'])
        
    # Copy to templates
    os.system(f"cp {py_path} {os.path.join(template_dir, data['file_name'])}")
    os.system(f"cp {test_path} {os.path.join(template_dir, f'test_{data['file_name']}')}")
    
    print(f"✅ Successfully created '{folder_name}'!")
    print(f"📁 Logic file: {py_path}")
    print(f"🧪 Test file : {test_path}")
    print(f"💾 Templates saved to: {template_dir}")
    print("\nRun `cd dsa_training && pytest` to start training!")

if __name__ == "__main__":
    main()
