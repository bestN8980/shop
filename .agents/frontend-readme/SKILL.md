---
name: frontend-readme
description: Generate a comprehensive, professional README.md file for frontend software projects. Use when the user asks to write, generate, create, or format a frontend project README or documentation.
---

## Instructions

Before writing the README, inspect the actual codebase provided by the user. Do not invent or assume information — every section below must be based on real files (e.g. `package.json`, config files, router setup, state management store, `.env.example`, API client code, `Dockerfile`, `LICENSE`).

If a section does not apply to the project (e.g. no authentication, no role-based UI, no screenshots provided), omit that section entirely instead of leaving it empty or filling it with placeholder text.

Keep the tone concise and professional. Use tables where the content is naturally tabular (environment variables, routes, tech stack).

## Project Title
- Name of the repository, taken from `package.json` or as specified by the user.

## Overview
- What the project is used for.
- The main purpose(s) of the project.
- How the frontend communicates with the backend (e.g. REST via Axios/Fetch, GraphQL, WebSocket), inferred from the actual API client code.

## Features
- Bullet list of the frontend's actual features, inferred from pages, components, and routes in the codebase.

## Tech Stack
- Identify from dependency files and imports: language/framework, build tool, state management, routing library, testing framework, HTTP client, UI library, and form validation library.
- Present as a short table or bullet list grouped by category.

## Architecture
- Describe the high-level structure and data flow (e.g. pages → components → hooks/services → API client → backend).
- Describe how state flows through the app (e.g. component state → global store → UI).
- Include a Mermaid diagram if the architecture has more than 2-3 layers.

## Project Structure
- Show the actual folder/file structure (as a code block tree) and briefly explain what each top-level folder is responsible for.

## Requirements
- List runtime/tooling requirements needed to run the project (e.g. Node.js version, package manager), taken from config files (`.nvmrc`, `engines` field, etc.) when available.

## Installation
- Actual bash commands to clone the repo and install dependencies, matching the project's package manager (npm/yarn/pnpm).

## Environment Variables
- Table with columns: Variable | Description | Example Value.
- Source these from `.env.example` or config-loading code — never invent variable names.

## Running Frontend
- Bash command(s) to run the dev server, taken from the actual scripts in `package.json`.

## API Integration
- Document: API base URL configuration, HTTP client used, authentication headers, request handling, response handling, and error handling — based on the actual API client/service files.

## Authentication
- Include this section only if the project has authentication. Document: login flow, register flow, token storage (e.g. localStorage, cookies), protected routes, logout, and role-based UI — based on the actual auth code.

## Routing
- Document public routes, protected routes, and admin routes (if applicable), based on the actual router configuration. A table of path → component → access level works well.

## Components
- List the main reusable/shared components, with a one-line description of each, based on the actual `components` folder.

## State Management
- Include this section only if the project uses a state management library/pattern beyond plain component state. Document the actual state slices used (e.g. global state, auth state, cart state), based on the actual store/context code.

## Styling / UI
- Document the actual UI library, CSS framework, CSS preprocessor, CSS methodology (e.g. BEM, CSS Modules, utility-first), and responsive design approach used in the project.

## Build
- Bash command to build the project for production, taken from `package.json` scripts.

## Deployment
- Bash command(s) or steps to deploy the project, based on actual deployment config found (e.g. `Dockerfile`, CI/CD config, hosting platform config). Omit if no deployment setup exists in the codebase.

## Screenshots / Demo
- Include this section only if the user provides screenshots, a demo link, or asks for placeholders explicitly.

## License
- State the project's actual license, read from the `LICENSE` file if present. If no license file exists, note that explicitly instead of defaulting to MIT.