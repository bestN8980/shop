# Shop

Shop is a full-stack e-commerce application with a React storefront and a FastAPI backend. The platform lets users browse products, add items to a cart, place orders, manage their profile, and access an admin dashboard for catalog and user management.

## Features

- Product catalog with search and category filtering in the frontend
- User registration and login with JWT authentication
- Protected routes for authenticated users and admin-only screens
- Shopping cart and checkout flow connected to backend order creation
- User profile updates, password changes, and avatar upload
- Admin dashboard for product, category, and user management
- Cloudinary-powered image uploads for avatars and products
- Docker Compose setup for local full-stack development

## Tech Stack

| Layer | Stack |
| --- | --- |
| Backend | Python, FastAPI, SQLAlchemy, MySQL, Pydantic |
| Frontend | React, Vite, React Router, Axios, Tailwind CSS |
| Auth | JWT via python-jose, OAuth2PasswordBearer, localStorage token storage in the browser |
| File storage | Cloudinary |
| Deployment | Docker, Docker Compose, Nginx for frontend static serving |
| Hosting config | Netlify redirect fallback for SPA routing |

## System Architecture

The project is composed of three main parts: the frontend UI, the FastAPI API, and MySQL. The browser sends API requests through Axios, the backend validates auth and business rules, and the data is persisted in MySQL. Product and avatar uploads are sent to Cloudinary.

```mermaid
flowchart LR
    A[Browser User] --> B[React Frontend]
    B --> C[Axios API client]
    C --> D[FastAPI backend]
    D --> E[SQLAlchemy models]
    E --> F[(MySQL)]
    D --> G[Cloudinary]
    B --> H[localStorage token]
```

## Project Structure

```text
shop/
├── app/
│   ├── core/
│   ├── dependencies/
│   ├── modules/
│   ├── scripts/
│   ├── .env
│   ├── .env.example (not present)
│   ├── Dockerfile
│   ├── LICENSE
│   ├── main.py
│   ├── README.md
│   └── requirements.txt
├── shop-fe/
│   ├── src/
│   ├── Dockerfile
│   ├── netlify.toml
│   ├── package.json
│   ├── README.md
│   ├── vite.config.js
│   └── tailwind.config.js
├── docker-compose.yml
├── package-lock.json
├── README.md
└── .dockerignore
```

### Top-level responsibilities

- `app/`: backend service and business logic
- `shop-fe/`: frontend UI and client-side routing
- `docker-compose.yml`: local orchestration for MySQL, backend, and frontend
- `package-lock.json`: lockfile for root-level package state if used by tooling

## Requirements

- Python 3.14 for the backend container/runtime
- Node.js 22 for the frontend Docker build and Vite dev workflow
- MySQL 8 for the database
- Docker and Docker Compose for the full stack runtime
- A Cloudinary account for file uploads

## Installation

Clone the repository and set up the backend and frontend separately:

```bash
cd shop

python3 -m venv app/venv
source app/venv/bin/activate
pip install -r app/requirements.txt

cd shop-fe
npm install
```

Create the backend environment file at `app/.env` before starting the app.

## Environment Variables

| Variable | Scope | Description | Example Value |
| --- | --- | --- | --- |
| `DATABASE_URL` | Backend | MySQL connection string | `mysql+pymysql://shop_user:108980@localhost:3306/shop` |
| `SECRET_KEY` | Backend | JWT signing secret | `super-secret-key` |
| `ALGORITHM` | Backend | JWT signing algorithm | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Backend | JWT lifetime in minutes | `30` |
| `CLOUDINARY_CLOUD_NAME` | Backend | Cloudinary cloud name | `demo` |
| `CLOUDINARY_API_KEY` | Backend | Cloudinary API key | `123456789012345` |
| `CLOUDINARY_API_SECRET` | Backend | Cloudinary API secret | `secret` |
| `VITE_API_URL` | Frontend | Base URL used by Axios for backend calls | `http://localhost:8000` |

The frontend falls back to `/api` if `VITE_API_URL` is not set, but the app is designed to point to the backend server directly in local development.

## Running the Application

### Backend

```bash
cd shop
source app/venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd shop/shop-fe
npm run dev
```

The frontend typically runs on port `5173`, while the backend serves Swagger at `http://localhost:8000/docs`.

### Full stack with Docker Compose

```bash
cd shop
docker compose up --build
```

This starts:

- MySQL on port `3307` (host) / `3306` (container)
- backend API on `:8000` inside the container network
- frontend static site on port `80`

## Application Workflow

A typical user flow in the app is:

1. A user visits the React app and signs up or logs in.
2. The frontend calls `/users/login` or `/users/register` through the Axios client.
3. The backend validates credentials, issues a JWT, and returns an access token.
4. The frontend stores the token in `localStorage` and uses it on protected requests.
5. Users can browse products, add items to their cart, and create an order from the current cart.
6. Admin users access a separate dashboard to manage products, categories, and user records.
7. Product and avatar images are uploaded through the backend to Cloudinary and rendered back in the UI.

## API

The backend exposes a REST API through FastAPI under the app module. The frontend consumes it via a centralized Axios instance from `shop-fe/src/services/api.js`.

High-level groups:

| Group | Purpose |
| --- | --- |
| `/users` | Register, login, profile, password update, avatar upload, admin user management |
| `/products` | Product listing and admin product CRUD |
| `/categories` | Category listing and admin CRUD |
| `/cart` | User cart retrieval, item additions, and removals |
| `/orders` | Order creation and user order history |
| `/uploads` | Image upload helper endpoint |

See [app/README.md](app/README.md) for the detailed backend API reference, and [shop-fe/README.md](shop-fe/README.md) for frontend usage details.

## Database

The application uses MySQL and SQLAlchemy models for a small e-commerce schema.

```mermaid
erDiagram
    USER ||--o{ CART : owns
    USER ||--o{ ORDER : places
    CATEGORY ||--o{ PRODUCT : contains
    CART ||--o{ CART_ITEM : contains
    PRODUCT ||--o{ CART_ITEM : appears_in
    ORDER ||--o{ ORDER_ITEM : contains
    PRODUCT ||--o{ ORDER_ITEM : appears_in

    USER {
        int id PK
        string username
        string email
        string hashed_password
        string full_name
        string phone
        string avatar_url
        string avatar_public_id
        enum role
        datetime created_at
        datetime updated_at
        bool is_deleted
    }

    CATEGORY {
        int id PK
        string name
        datetime created_at
    }

    PRODUCT {
        int id PK
        string name
        string description
        int price
        int stock
        int category_id FK
        string image_url
        string image_public_id
        bool is_deleted
        datetime created_at
        datetime updated_at
    }

    CART {
        int id PK
        int user_id FK
    }

    CART_ITEM {
        int id PK
        int cart_id FK
        int product_id FK
        int quantity
        int price
    }

    ORDER {
        int id PK
        int user_id FK
        float total_price
        string status
        datetime created_at
    }

    ORDER_ITEM {
        int id PK
        int order_id FK
        int product_id FK
        int quantity
        float price
    }
```

## Authentication & Authorization

The authentication flow is JWT-based in the backend and context-based in the frontend.

- The frontend uses `AuthContext` to store the current user and token.
- On login, the backend returns `access_token` and `token_type`.
- The token is stored in `localStorage` and attached to requests through Axios.
- Protected routes in the frontend redirect unauthenticated users to `/login`.
- The backend uses `OAuth2PasswordBearer` and `get_current_user()` to validate each request.
- Role enforcement is handled through `require_role([...])`, with `USER` and `ADMIN` roles defined in the backend enum.

## File / Image Upload

The app includes image upload support through Cloudinary.

- User avatar updates and product image uploads are processed by the backend.
- The helper uploads to Cloudinary and stores the returned `url` and `public_id`.
- Upload routes are defined under the backend’s uploads module.
- Supported files are image uploads in the browser and backend upload endpoint.

## Docker

The repository contains a Docker Compose configuration that wires together the app stack.

```yaml
services:
  mysql:
    image: mysql:8.0
  backend:
    build: ./app
  frontend:
    build: ./shop-fe
```

It provides:

- MySQL persistence via a named Docker volume
- backend service from `app/Dockerfile`
- frontend static server built from `shop-fe/Dockerfile`

Run it with:

```bash
cd shop
docker compose up --build
```

## Deployment

The project has deployment setup for both the frontend and the backend stack:

- The backend is containerized via `app/Dockerfile`.
- The frontend is containerized and served with Nginx via `shop-fe/Dockerfile` and `shop-fe/nginx.conf`.
- The frontend includes a Netlify redirect rule in `shop-fe/netlify.toml` to support client-side routes.
- The compose stack wires the app together for local deployment and testing.

## Documentation

- Backend documentation: [app/README.md](app/README.md)
- Frontend documentation: [shop-fe/README.md](shop-fe/README.md)
- Root project overview: [README.md](README.md)

## Screenshots

### Product List

![Product List](./screenshots/products.png)

### Login

![Login Page](./screenshots/login.png)

### Admin Dashboard

![Admin Dashboard](./screenshots/admin.png)

## Troubleshooting

Common issues you may hit with this stack:

- Missing `app/.env` values will prevent backend startup or JWT issuance.
- MySQL not running or wrong `DATABASE_URL` will break app startup.
- Frontend login failures often come from the backend not running or `VITE_API_URL` pointing to the wrong host.
- Port conflicts on `3307`, `8000`, or `5173` can block local startup.
- Cloudinary upload errors usually mean the cloud credentials are missing or invalid.

## License

The project code is licensed under the MIT License. See [app/LICENSE](app/LICENSE) for the full text.
