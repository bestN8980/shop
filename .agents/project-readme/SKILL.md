---
name: project-readme
description: Generate a comprehensive, professional README.md file for a full-stack project's root/parent folder that contains both a backend (be) and frontend (fe) subfolder. Use when the user asks to write, generate, create, or format a top-level/root README for a project that has separate backend and frontend directories.
---

## Instructions

Before writing the README, inspect the actual codebase in both the backend subfolder and the frontend subfolder provided by the user. Do not invent or assume information — every section below must be based on real files (e.g. `package.json`, `requirements.txt`, config files, router setup, models/migrations, `.env.example`, `Dockerfile`, `docker-compose.yml`, CI config, test files, `LICENSE`).

This README describes the project as a whole (both `be/` and `fe/` together) — keep it at a higher level than the individual backend/frontend READMEs. Link out to `be/README.md` and `fe/README.md` for deep implementation details when they exist, rather than duplicating everything here.

If a section does not apply to the project (e.g. no Docker setup, no screenshots), omit that section entirely instead of leaving it empty or filling it with placeholder text.

Keep the tone concise and professional. Use tables where the content is naturally tabular (environment variables, API summary, tech stack). Use Mermaid diagrams for architecture and database sections when helpful.

## 1. Overview
- Project name, what it is used for, and its main purpose(s).
- One or two sentences on the overall product, not just the code.

## 2. Features
- Bullet list of the product's actual features, inferred from both backend routes/business logic and frontend pages/components.

## 3. Tech Stack
- Table split into Backend and Frontend columns (or two sub-lists): language, framework, database, ORM, auth, validation, file storage, testing, build tool, state management, routing, UI library, and infrastructure — identified from each subfolder's dependency files.

## 4. System Architecture
- Describe how the frontend, backend, database, and any external services interact as a whole system.
- Include a Mermaid diagram (client → frontend → API → backend → database/external services) if the system has more than 2-3 components.

## 5. Project Structure
- Show the root-level folder structure as a code block tree (e.g. `be/`, `fe/`, shared configs, CI files), with a one-line description of each top-level folder. Do not repeat the internal structure already covered inside `be/README.md` or `fe/README.md`.

## 6. Requirements
- List runtime/tooling requirements needed to run the whole project (e.g. Node.js version, Python version, database engine, Docker), taken from config files in both subfolders.

## 7. Installation
- Step-by-step setup for the whole project: clone repo → install backend dependencies → install frontend dependencies → set up database → configure environment variables (both be/fe) → run migrations → (optionally) start via Docker Compose.
- Provide actual bash commands matching the project's package managers.

## 8. Environment Variables
- Table with columns: Variable | Scope (Backend/Frontend) | Description | Example Value.
- Source these from each subfolder's `.env.example` — never invent variable names.

## 9. Running the Application
- Bash commands to run backend and frontend together in development (and production if applicable), including the order to start them and default ports.

## 10. Application Workflow
- Describe a typical end-to-end user flow through the system (e.g. user action in UI → frontend request → backend processing → database → response → UI update), based on the actual code, not a generic example.

## 11. API
- High-level summary of the API surface: base URL, versioning, and a table of key endpoint groups with a link/reference to full API docs (`be/README.md` or a dedicated API doc) rather than repeating every endpoint here.

## 12. Database
- Mermaid ER diagram describing the actual schema (entities, fields, relationships), based on models/migrations found in the backend.

## 13. Authentication & Authorization
- Tech stack used (e.g. JWT, sessions, OAuth).
- Describe the end-to-end auth flow across both frontend and backend (login UI → API call → token issuance → token storage → protected routes/middleware → role-based access).

## 14. File / Image Upload
- Include this section only if the project has an upload feature. Cover: upload flow (frontend → backend → storage), storage provider, supported formats, maximum file size, and the returned URL/response format.

## 15. Docker
- Include this section only if Docker/Docker Compose files exist. Describe the services defined (backend, frontend, database, etc.), how to build and run them, and key ports/volumes.

## 16. Deployment
- Cover whichever of the following actually apply, based on real config found: hosting platform, reverse proxy, environment configuration per environment (staging/production), CI/CD pipeline, and external services used in production.

## 17. Documentation
- Links to any additional docs that exist in the repo (e.g. `be/README.md`, `fe/README.md`, API reference, architecture decision records, Postman/Swagger collection).

## 18. Screenshots / Demo
- Include this section only if the user provides screenshots, a demo link, or explicitly asks for placeholders.

## 19. Testing
- Describe how to run tests for backend and frontend separately, and the testing frameworks used in each, based on actual test scripts/config found.

## 20. Troubleshooting
- Common setup issues actually likely for this stack (e.g. port conflicts, missing env variables, migration errors) — only include items that are genuinely relevant to the detected stack, not generic filler.

## 21. License
- State the project's actual license, read from the `LICENSE` file if present. If no license file exists, note that explicitly instead of defaulting to MIT.