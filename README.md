# lucas-quality-ai-portfolio

This is a full-stack portfolio project focused on Quality Engineering, Test Automation, DevOps, and AI. The goal is to demonstrate senior-level technical skills by delivering a complete system architecture including:

- FastAPI-based backend (Python)
- Async processing with queues and cloud services
- Minimal front-end for E2E test scenarios
- Automated test coverage (unit, component, contract, performance, security)
- CI/CD pipelines with rollback and dynamic test containers
- AI-driven unit test generation using OpenAI API

---

## 📑 Technical Backlog

### 🧠 Stage 0 – Product Story

| ID  | Title                                  | Type     | Goal                                                    | Acceptance Criteria                              |
|-----|----------------------------------------|----------|---------------------------------------------------------|--------------------------------------------------|
| T0  | Define the product story and scope     | Product  | Align narrative, technical value, and use-case logic    | Clear, realistic and cohesive product description |

---

### 🧱 Stage 1 – Initial Setup and Upload

| ID  | Title                                          | Type     | Goal                                                      | Acceptance Criteria                             |
|-----|------------------------------------------------|----------|-----------------------------------------------------------|-------------------------------------------------|
| T1  | Create initial project structure               | Infra    | Scalable modular folder setup                             | Structured folders + initial README             |
| T2  | Implement healthcheck endpoint (`/status`)     | Backend  | Minimal FastAPI base running                              | Returns `{"status": "ok"}`                      |
| T3  | Upload CSV route with basic validation         | Backend  | Entry point for financial data                            | Validates and stores file in mocked S3          |
| T4  | Simulate async processing via local worker     | Backend  | Emulate queue/worker behavior for file consumption        | Worker consumes file and returns a result       |

---

### 🧮 Stage 2 – Scoring and AI

| ID  | Title                                           | Type         | Goal                                                      | Acceptance Criteria                                          |
|-----|-------------------------------------------------|--------------|-----------------------------------------------------------|--------------------------------------------------------------|
| T5  | Implement traditional score calculation         | Backend      | Rule-based credit scoring logic                           | Returns score, category and explanation                     |
| T6  | Integrate AI-based scoring via OpenAI API       | Backend/AI   | Intelligent scoring using LLM with fallback strategy      | Schema validation + fallback + cost control logic            |
| T7  | Generate unit tests automatically using OpenAI  | AI/Quality   | Generate pytest cases from function docstrings            | AI suggests valid test cases with 80%+ utility coverage      |

---

### 🧪 Stage 3 – Testing Strategies

| ID  | Title                                        | Type     | Goal                                                        | Acceptance Criteria                                       |
|-----|----------------------------------------------|----------|-------------------------------------------------------------|-----------------------------------------------------------|
| T8  | Create unit tests with `pytest`              | Quality  | Cover business logic (ScoreInput → ScoreOutput)             | Pass/fail output validation + equivalence partitioning    |
| T9  | Create component tests for endpoints         | Quality  | Test route logic without DB or queue interaction            | Valid status, content, schema per route                   |
| T10 | Setup contract tests with Pact               | Quality  | Validate integration between front and backend              | Consumer contract satisfied by provider                   |
| T11 | Create E2E tests with Playwright             | Quality  | Simulate real browser interaction via front-end             | Simulated user flow tested and validated                  |
| T12 | Add performance tests with k6                | Quality  | Measure throughput, latency, and system degradation         | Metrics generated + limits respected                      |
| T13 | Add security scan via OWASP ZAP              | Quality  | Detect basic OWASP Top 10 issues via pipeline               | Report generation with no high-severity vulnerabilities   |

---

### 🚀 Stage 4 – CI/CD and Deployment

| ID  | Title                                       | Type      | Goal                                                  | Acceptance Criteria                                           |
|-----|---------------------------------------------|-----------|-------------------------------------------------------|---------------------------------------------------------------|
| T14 | Create CI workflow for pre-deploy testing   | DevOps    | Test on PR/push before building/deploying             | Lint, unit, component, contract tests must pass               |
| T15 | Create CD pipeline with rollback logic      | DevOps    | Deploy only on success, rollback on failure           | GitHub Actions deploys + reverts on test failure              |
| T16 | Run tests in dynamic container environments | DevOps    | Ensure isolation for parallel runs                    | Each job runs in independent container, with clean teardown   |

---

### ☁️ Stage 5 – Cloud Integrations

| ID  | Title                                | Type    | Goal                                        | Acceptance Criteria                                   |
|-----|--------------------------------------|---------|---------------------------------------------|-------------------------------------------------------|
| T17 | Integrate AWS S3 (or mock)           | Cloud   | Store raw uploaded financial CSVs           | File available for processing                         |
| T18 | Integrate Lambda-like service        | Cloud   | Simulate async processing in isolated logic | Triggered and returns processed payload               |
| T19 | Integrate mock or real RDS/DB        | Cloud   | Store processed score data for history      | Queries return consistent and correct data            |

---
