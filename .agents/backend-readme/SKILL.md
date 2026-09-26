---
name: backend-readme
description: Generate a comprehensive, professional README.md file for backend software projects. Use when the user asks to write, generate, create, or format a backend project README or documentation.
---

## Instructions

Before writing the README, inspect the actual codebase provided by the user. Do not invent or assume information — every section below must be based on real files (e.g. `package.json`, `requirements.txt`, `go.mod`, `pom.xml`, config files, models, routes/controllers, migrations, `.env.example`, `Dockerfile`, `docker-compose.yml`, `LICENSE`).

If a section does not apply to the project (e.g. no file upload feature), omit that section entirely instead of leaving it empty or filling it with placeholder text.

Keep the tone concise and professional. Use tables where the content is naturally tabular (environment variables, API endpoints, tech stack).

## Title
- Name of the repository, taken from the project folder name, `package.json`/`pyproject.toml`, or as specified by the user.

## Overview
- What the project is used for.
- The main purpose(s) of the project.
- 2-4 sentences max.

## Features
- Bullet list of the backend's actual features, inferred from routes, modules, and business logic in the codebase.

## Tech Stack
- Identify from dependency files and imports: language, framework, database, ORM/query builder, authentication library, validation library, file storage, testing framework, and infrastructure/deployment tools.
- Present as a short table or bullet list grouped by category.

## Architecture
- Describe the high-level request flow (e.g. client → router → controller → service → repository → database).
- Include a Mermaid flowchart diagram if the architecture has more than 2-3 layers.

## Project Structure
- Show the actual folder/file structure (as a code block tree) and briefly explain what each top-level folder is responsible for.

## Requirements
- List runtime/tooling requirements needed to run the project (e.g. Node.js version, Python version, database engine, package manager), taken from config files (`.nvmrc`, `engines` field, `pyproject.toml`, etc.) when available.

## Installation
- Step-by-step, in order: clone repo → create virtual environment (if applicable) → install dependencies → set up database → configure environment variables → run migrations → start server.
- Provide actual bash commands, not generic placeholders, matching the project's package manager and stack.

## Environment Variables
- Table with columns: Variable | Description | Example Value.
- Source these from `.env.example` or config-loading code — never invent variable names.

## Running Backend
- Bash commands to run the server in development and (if applicable) production mode.

## API Documentation
- For each endpoint: HTTP method, path, brief description, request parameters/body, response format, and one example request/response.
- Group endpoints by resource/module using subheadings. Use tables for parameters where possible.

## Database
- Mermaid ER diagram describing the actual schema (entities, fields, relationships), based on models/migrations found in the codebase.

## Authentication & Authorization
- Tech stack used (e.g. JWT, sessions, OAuth, Passport, Devise).
- Describe the actual auth flow found in the code (login → token issuance → middleware validation → role/permission checks).

## File/Image Upload
- Include this section only if the project has an upload feature. Cover: upload flow, storage provider (local/S3/Cloudinary/etc.), supported formats, maximum file size, and the returned URL/response format.

## Deployment
- Cover whichever of the following actually apply to the project: Docker, Docker Compose, reverse proxy, environment configuration, production server setup, external/third-party services.

## License
- State the project's actual license, read from the `LICENSE` file if present. If no license file exists, note that explicitly instead of defaulting to MIT.