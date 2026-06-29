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

## ⚙️ Workflow: PR-Driven Question Authoring

To maintain high-quality training data and build a professional portfolio history, **direct commits to the `main` branch are strictly prohibited.** All new questions must be added via Pull Requests (PR).

1. **Create a Branch**: `git checkout -b feature/add-binary-search-question`
2. **Author the Question**: Create a new `.md` file in the `content/` directory following the required format (`# Prompt`, `# Buggy Code`, `# Solution`).
3. **Submit a PR**: Use the provided PR template to document the **Intended Edge Cases** and performance bottlenecks you designed.
4. **Merge & Auto-Deploy**: Once merged into `main`, Cloudflare Pages automatically rebuilds the static payload (`questions.js`) and deploys to production.

## 🏗️ Architecture
- **Data Pipeline**: Python script (`build.py`) parses Markdown files and compiles them into a static JSON/JS payload.
- **Frontend**: Cloudflare Pages (Serving static HTML & compiled JS).
- **Backend API**: Cloudflare Pages Functions (`functions/api/`).
- **Database**: Cloudflare D1 (SQLite).
