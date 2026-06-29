DROP TABLE IF EXISTS evaluations;
CREATE TABLE evaluations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id TEXT NOT NULL,
    time_remaining INTEGER NOT NULL,
    logic_bug_feedback TEXT,
    complexity_feedback TEXT,
    final_feedback TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
