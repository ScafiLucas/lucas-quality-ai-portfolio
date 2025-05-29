CREATE TABLE IF NOT EXISTS credit_scores (
    id SERIAL PRIMARY KEY,
    score INTEGER NOT NULL,
    category VARCHAR(50) NOT NULL,
    explanation VARCHAR(255) NOT NULL,
    job_id VARCHAR(100) NOT NULL
);
