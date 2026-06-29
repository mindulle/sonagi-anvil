# 🔨 Sonagi Anvil 

> "AI Code Review Assessment Training Platform"

An interactive, self-hosted training platform designed to sharpen code review skills, specifically targeting AI-generated code evaluations (e.g., Outlier, Alignerr).

## 🛡️ Core Engineering Principles

This project strictly adheres to the following rules to ensure a robust and maintainable architecture:

1. **Serverless First (Zero Ops)**: No dedicated servers. The entire architecture runs seamlessly on the Cloudflare Ecosystem (Pages + Functions + D1) incurring $0 in maintenance costs.
2. **Strict SSOT (Single Source of Truth) Separation**:
   - **Questions Data**: Maintained purely as local Markdown files in `content/` to leverage Git version control. No database overhead for static content.
   - **Evaluation Records**: Stored in Cloudflare D1 (Serverless SQLite) to track user progress and feedback history. State and data are strictly separated.
3. **Vanilla UI (Ultra-Lightweight Frontend)**: Built with pure HTML/JS/CSS without heavy frameworks like React or Next.js, ensuring blazing fast load times (< 0.1s) to maximize training focus.

## 🏗️ Architecture

- **Data Pipeline**: Python script (`build.py`) parses Markdown files and compiles them into a static JSON/JS payload during the CI/CD build phase.
- **Frontend**: Cloudflare Pages (Serving static HTML & compiled JS).
- **Backend API**: Cloudflare Pages Functions (`functions/api/`).
- **Database**: Cloudflare D1 (SQLite).

## 🚀 How to Add a Training Scenario

1. Create a new `.md` file in the `content/` directory.
2. Follow the required sections: `# Prompt`, `# Buggy Code`, and `# Solution`.
3. Commit and push. Cloudflare Pages will automatically rebuild and deploy the new training set.
