# Sonagi Anvil Development Skill
이 스킬은 `sonagi-anvil` 프로젝트에서 작업하는 AI 에이전트를 위한 절대 지침입니다.

## 🚨 [CRITICAL] Git Workflow (PR Forced)
1. **Never push to main**: `main` 브랜치는 GitHub Protection Rule에 의해 보호됩니다. `git push origin main`을 시도하면 서버 에러가 발생합니다.
2. **PR-Driven Workflow**: 새로운 문제 추가나 코드 수정 시 반드시 아래 절차를 따르십시오.
   - `git checkout -b <브랜치명>` (예: `feature/add-two-sum`)
   - 코드 작성 및 커밋
   - `git push -u origin <브랜치명>`
   - `gh pr create --fill` 명령어를 사용하여 Pull Request를 반드시 생성하십시오.

## 🏗️ Architecture & Tech Stack Rules
1. **Serverless First**: 서버 인스턴스 구축 금지. 모든 백엔드는 Cloudflare (Pages + Functions + D1) 인프라로만 구성하십시오.
2. **Vanilla UI**: 무거운 프레임워크(React, Next.js 등)의 무단 도입을 금지합니다. HTML/JS/CSS 기반의 초경량 뷰어를 유지하십시오.
3. **SSOT (Single Source of Truth)**: 훈련용 문제 데이터는 오직 `content/` 디렉토리 내의 마크다운(`.md`) 파일로만 관리하십시오.

## 📝 Problem Authoring Format
새로운 문제를 `content/` 에 추가할 때는 다음 마크다운 섹션을 반드시 포함해야 빌드 스크립트(`build.py`)가 정상 작동합니다.
- `# Prompt`: 문제의 요구사항
- `# Buggy Code`: `python` 또는 `javascript` 코드 블록 안에 엣지 케이스를 놓친 AI의 버그 코드
- `# Solution`: 논리 버그, Big O 최적화, 영어 피드백 템플릿 포함

## 🧪 DSA Training Pipeline (TDD)
1. **Workspace**: 알고리즘 문제 풀이 및 실기 훈련은 반드시 `dsa_training/` 디렉토리 하위에서 진행하십시오.
2. **TDD 강제**: 문제를 풀 때 로직 구현 파일(예: `two_sum.py`)과 테스트 파일(예: `test_two_sum.py`)을 함께 작성하십시오.
3. **Local Validation**: 코드를 커밋하기 전, 반드시 로컬에서 `cd dsa_training && pytest`를 실행하여 모든 테스트가 통과(PASS)하는지 확인하십시오. 테스트를 통과하지 못한 코드는 PR을 생성할 수 없습니다.
4. **CI/CD 연동**: PR을 생성하면 GitHub Actions를 통해 `DSA Pytest CI`가 자동으로 실행됩니다.
