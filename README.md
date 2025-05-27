# lucas-quality-ai-portfolio

This is a full-stack portfolio project focused on Quality Engineering, Test Automation, DevOps, and AI. The goal is to demonstrate senior-level technical skills by delivering a complete system architecture including:

- FastAPI-based backend (Python)
- Async processing with queues and cloud services
- Minimal front-end for E2E test scenarios
- Automated test coverage (unit, component, contract, performance, security)
- CI/CD pipelines with rollback and dynamic test containers
- AI-driven unit test generation using OpenAI API

---

## 📋 Technical Backlog

### 🧠 Stage 0 – Product Story

| ID  | Title                                               | Type     | Goal                                                  | Acceptance Criteria                                  |
|-----|-----------------------------------------------------|----------|-------------------------------------------------------|------------------------------------------------------|
| T0  | Define the product story and functional scope       | Product  | Align narrative, technical value, and use-case logic  | Clear, realistic and cohesive product description     |

---

### 🚀 Stage 1 – Initial Setup and Upload

| ID  | Title                                               | Type     | Goal                                                  | Acceptance Criteria                                  |
|-----|-----------------------------------------------------|----------|-------------------------------------------------------|------------------------------------------------------|
| T1  | Create initial project structure                    | Infra    | Scalable modular folder setup                         | Structured folders + initial empty README             |
| T2  | Implement base FastAPI endpoint (`/status`)         | Backend  | Minimal healthcheck API                               | Returns `{"status": "ok"}`                           |
| T3  | Upload CSV route with basic validation              | Backend  | Entry point for financial data                        | Validates and stores file in mocked S3               |
| T4  | Simulate async processing via local worker          | Backend  | Mock queue behavior                                   | Worker consumes file and returns a result            |

---

### 🧮 Stage 2 – Scoring and AI

| ID  | Title                                               | Type     | Goal                                                  | Acceptance Criteria                                  |
|-----|-----------------------------------------------------|----------|-------------------------------------------------------|------------------------------------------------------|
| T5  | Implement traditional score calculation             | Backend  | Rule-based credit scoring                             | Returns numeric score + justification                |
| T6  | Integrate AI-based scoring via OpenAI               | Backend/AI | AI-driven scoring with fallback                       | Schema validation + fallback + cost control          |

---

### 🌐 Stage 3 – Front-End and UX

| ID  | Title                                               | Type     | Goal                                                  | Acceptance Criteria                                  |
|-----|-----------------------------------------------------|----------|-------------------------------------------------------|------------------------------------------------------|
| T7  | Build basic front-end for upload and status         | Frontend | HTML/JS front-end for testing E2E flows               | File upload and score display                        |

---

### 🧪 Stage 4 – Test Coverage

| ID  | Title                                               | Type     | Goal                                                  | Acceptance Criteria                                  |
|-----|-----------------------------------------------------|----------|-------------------------------------------------------|------------------------------------------------------|
| T8  | Unit tests for score logic                          | QA       | Base-level logic coverage                             | Pytest with coverage                                 |
| T9  | Component tests mocking external dependencies       | QA       | Integration without real infra                        | Mock S3, queue and database                          |
| T10 | E2E tests with Selenium or Playwright               | QA       | Full flow testing via UI                              | Runs in headless browser                             |
| T11 | Contract tests using Pact                           | QA       | Validate consumer/provider interactions               | Versioned and validated contract                     |

---

### ⚙️ Stage 5 – Performance, Security and Infra

| ID  | Title                                               | Type     | Goal                                                  | Acceptance Criteria                                  |
|-----|-----------------------------------------------------|----------|-------------------------------------------------------|------------------------------------------------------|
| T12 | Performance tests with Locust                       | QA       | Load validation for processing endpoints              | Simulates large-scale usage                          |
| T13 | Security tests using OWASP ZAP CLI                  | QA       | Basic vulnerability scanning                          | Auto-scan with exportable report                     |
| T14 | Dockerize backend, worker, and front-end            | DevOps   | Run everything in isolated containers                 | `docker-compose` with `.env` support                 |

---

### 🔁 Stage 6 – CI/CD & Environments

| ID  | Title                                               | Type     | Goal                                                  | Acceptance Criteria                                  |
|-----|-----------------------------------------------------|----------|-------------------------------------------------------|------------------------------------------------------|
| T15 | Create GitHub Actions pipeline with pre/post checks | CI/CD    | Validate build, lint, and test on push/PR             | GH Actions runs on commits                           |
| T16 | Implement automatic rollback on failed post-deploy  | CI/CD    | Ensure safe deploys with self-healing                 | Rollback triggered on failure                        |
| T17 | Setup dynamic container environments for testing    | CI/CD    | Isolated environments on demand                       | Spin-up and teardown controlled                      |

---

### 🤖 Stage 7 – AI and Cloud Integration

| ID  | Title                                               | Type     | Goal                                                  | Acceptance Criteria                                  |
|-----|-----------------------------------------------------|----------|-------------------------------------------------------|------------------------------------------------------|
| T18 | Script for AI-based unit test generation            | AI       | Generate unit tests using docstrings and OpenAI       | Cached responses, clean format                       |
| T19 | Replace local queue with AWS SQS and Lambda         | Cloud    | Move to real async infrastructure                     | Lambda triggered by SQS, writes to DB                |
| T20 | Document full architecture and tech overview        | Doc      | Make the project visually and technically self-contained | Visual diagrams + badges + instructions              |
