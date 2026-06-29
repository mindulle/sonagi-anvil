# Contributing to Sonagi Anvil

Welcome to the `sonagi-anvil` repository! This platform is strictly maintained to ensure a high-quality, professional Git workflow.

## 🤖 Rules for AI Agents (Important)
If you are an AI Assistant or Autonomous Agent executing tasks in this repository, **you MUST strictly adhere to the following rules:**

1. **NO DIRECT PUSH TO MAIN**: The `main` branch is fully protected. Any attempt to run `git push origin main` will be rejected by the server.
2. **USE PR WORKFLOW**:
   - Always create a new branch: `git checkout -b <branch-name>`
   - Commit your changes.
   - Push your branch: `git push -u origin <branch-name>`
   - Create a Pull Request using the GitHub CLI: `gh pr create --fill`
3. **DO NOT MODIFY ARCHITECTURE**: Do not introduce heavy frameworks (e.g., React, Next.js) or external DBs. Respect the Serverless/Vanilla JS/D1 architecture.

## 🧑‍💻 How to Add a New Question
1. Create a new branch.
2. Add a new Markdown file in the `content/` directory.
3. Ensure it contains `# Prompt`, `# Buggy Code`, and `# Solution` sections.
4. Open a Pull Request and fill out the provided PR template.
