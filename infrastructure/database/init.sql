CREATE TABLE IF NOT EXISTS credit_scores (
    id SERIAL PRIMARY KEY,
    score INTEGER NOT NULL,
    category VARCHAR(50) NOT NULL,
    explanation VARCHAR(255) NOT NULL,
    job_id VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS credit_score_inputs (
    id SERIAL PRIMARY KEY,
    income FLOAT NOT NULL,
    debt FLOAT NOT NULL,
    savings FLOAT NOT NULL,
    late_payments INT NOT NULL,
    job_id VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS job_tracker (
    id SERIAL PRIMARY KEY,
    job_id VARCHAR(100) UNIQUE NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'pending'
);
