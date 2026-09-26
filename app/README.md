# ShopApp Backend

FastAPI-based backend for the ShopApp e-commerce application. It exposes REST APIs for user authentication, product and category management, cart operations, and order creation, and it stores data in MySQL through SQLAlchemy.

## Features

- User registration, login, profile update, password changes, and avatar upload
- JWT-based authentication with role checks for regular users and admins
- Product catalog management with image uploads to Cloudinary
- Category CRUD for admin users
- Per-user cart creation, item addition, and cart item removal
- Order creation from a user cart and retrieval of order history
- Admin-only user listing and soft-delete operations
- Automatic MySQL schema creation on startup for the app models

## Tech Stack

| Category | Stack |
| --- | --- |
| Language | Python 3.14 |
| API framework | FastAPI |
| Database | MySQL 8 |
| ORM | SQLAlchemy 2 |
| Auth | JWT via python-jose, OAuth2PasswordBearer |
| Password hashing | passlib + argon2 |
| Validation | Pydantic |
| File storage | Cloudinary |
| ASGI server | Uvicorn |
| Deployment | Docker, Docker Compose |

## Architecture

The backend follows a layered request flow:

Client → Router → Service → Repository → SQLAlchemy Model → MySQL

```mermaid
flowchart LR
    A[Client / Frontend] --> B[FastAPI Router]
    B --> C[Service Layer]
    C --> D[Repository Layer]
    D --> E[SQLAlchemy Models]
    E --> F[(MySQL)]
    G[Auth Middleware / RBAC] --> B
    H[Cloudinary Uploads] --> C
```

Key implementation files:

- `app/main.py` initializes the FastAPI app and includes routers.
- `app/dependencies/auth.py` validates JWT access tokens.
- `app/dependencies/rbac.py` enforces role-based access.
- `app/modules/*/service.py` implements business logic.
- `app/modules/*/repository.py` handles database operations.

## Project Structure

```text
shop/
├── app/
│   ├── core/
│   │   ├── cloudinary.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── enums.py
│   │   └── security.py
│   ├── dependencies/
│   │   ├── auth.py
│   │   ├── database.py
│   │   └── rbac.py
│   ├── modules/
│   │   ├── carts/
│   │   │   ├── model.py
│   │   │   ├── repository.py
│   │   │   ├── router.py
│   │   │   ├── schema.py
│   │   │   └── service.py
│   │   ├── categories/
│   │   │   ├── model.py
│   │   │   ├── repository.py
│   │   │   ├── router.py
│   │   │   ├── schema.py
│   │   │   └── service.py
│   │   ├── orders/
│   │   │   ├── model.py
│   │   │   ├── repository.py
│   │   │   ├── router.py
│   │   │   ├── schema.py
│   │   │   └── service.py
│   │   ├── products/
│   │   │   ├── model.py
│   │   │   ├── repository.py
│   │   │   ├── router.py
│   │   │   ├── schema.py
│   │   │   └── service.py
│   │   ├── uploads/
│   │   │   ├── router.py
│   │   │   └── service.py
│   │   └── users/
│   │       ├── admin_router.py
│   │       ├── model.py
│   │       ├── repository.py
│   │       ├── router.py
│   │       ├── schema.py
│   │       └── service.py
│   ├── scripts/
│   │   └── seed_admin.py
│   ├── .env
│   ├── Dockerfile
│   ├── LICENSE
│   ├── main.py
│   ├── README.md
│   └── requirements.txt
├── docker-compose.yml
├── shop-fe/
└── README.md
```

### Top-level responsibilities

- `app/core`: shared configuration, DB, JWT/security helpers, and Cloudinary setup.
- `app/dependencies`: auth and authorization guards used by router functions.
- `app/modules`: domain modules for users, products, categories, carts, orders, and uploads.
- `app/scripts`: setup helpers such as admin bootstrap.
- `docker-compose.yml`: orchestrates MySQL, backend, and frontend services.

## Requirements

- Python 3.14 (used in `app/Dockerfile`)
- MySQL 8 service running locally or via Docker Compose
- `pip` for dependency installation
- Access to valid Cloudinary credentials for image uploads

## Installation

```bash
cd shop
python3 -m venv app/venv
source app/venv/bin/activate
pip install -r app/requirements.txt
```

Create and populate the environment file:

```bash
cp app/.env app/.env.local
```

Then edit `app/.env` with the correct values. A working example is already present in the repo and includes:

```env
DATABASE_URL=mysql+pymysql://shop_user:108980@localhost:3306/shop
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret
```

Make sure the MySQL database `shop` exists before starting the app.

## Environment Variables

| Variable | Description | Example Value |
| --- | --- | --- |
| `DATABASE_URL` | SQLAlchemy connection string for the MySQL database | `mysql+pymysql://shop_user:108980@localhost:3306/shop` |
| `SECRET_KEY` | Secret used to sign JWT tokens | `super-secret-key` |
| `ALGORITHM` | JWT signing algorithm | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Duration for a generated JWT | `30` |
| `CLOUDINARY_CLOUD_NAME` | Cloudinary account cloud name | `demo` |
| `CLOUDINARY_API_KEY` | Cloudinary public API key | `123456789012345` |
| `CLOUDINARY_API_SECRET` | Cloudinary API secret | `secret` |

## Running Backend

Run the API in development mode:

```bash
cd shop
source app/venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open the API docs at:

- `http://localhost:8000/docs`
- `http://localhost:8000/redoc`

Run with Docker Compose from the repo root:

```bash
cd shop
docker compose up --build
```

This starts MySQL, the API backend, and the frontend in one stack.

## API Documentation

### Users

| Method | Path | Description | Auth |
| --- | --- | --- | --- |
| `POST` | `/users/register` | Register a new user | No |
| `POST` | `/users/login` | Login with email/password and get a JWT | No |
| `GET` | `/users/me` | Fetch the current authenticated user | Yes |
| `PUT` | `/users/me` | Update the authenticated user profile | Yes |
| `PUT` | `/users/change-password` | Change the current user password | Yes |
| `PUT` | `/users/me/avatar` | Upload and replace the user avatar | Yes |
| `GET` | `/users/admin/users` | List all non-deleted users | Admin |
| `DELETE` | `/users/admin/users/{user_id}` | Soft-delete a user | Admin |
| `POST` | `/users/login/oauth2` | OAuth2-style login endpoint for form-based username/password | No |

Example login request:

```json
{
  "email": "admin@example.com",
  "password": "secret123"
}
```

Example login response:

```json
{
  "access_token": "<jwt-token>",
  "token_type": "bearer"
}
```

### Products

| Method | Path | Description | Auth |
| --- | --- | --- | --- |
| `POST` | `/products/` | Create a product with optional image upload | Admin |
| `PUT` | `/products/{product_id}` | Update a product | Admin |
| `DELETE` | `/products/{product_id}` | Soft-delete a product | Admin |
| `GET` | `/products/` | List all active products | No |

The create-product route accepts form fields: `name`, `description`, `price`, `stock`, `category_id`, and optional `file`.

### Categories

| Method | Path | Description | Auth |
| --- | --- | --- | --- |
| `POST` | `/categories/` | Create a category | Admin |
| `PUT` | `/categories/{category_id}` | Update a category | Admin |
| `DELETE` | `/categories/{category_id}` | Delete a category | Admin |
| `GET` | `/categories/` | List all categories | No |

### Cart

| Method | Path | Description | Auth |
| --- | --- | --- | --- |
| `GET` | `/cart/` | View the authenticated user's cart | Yes |
| `POST` | `/cart/items` | Add a product to cart | Yes |
| `DELETE` | `/cart/items/{item_id}` | Remove one cart item | Yes |

Example add-to-cart payload:

```json
{
  "product_id": 2,
  "quantity": 1
}
```

### Orders

| Method | Path | Description | Auth |
| --- | --- | --- | --- |
| `POST` | `/orders/` | Create an order from the current cart | Yes |
| `GET` | `/orders/` | List the authenticated user's orders | Yes |

Example create-order payload:

```json
{
  "cart_id": 1
}
```

### Uploads

| Method | Path | Description | Auth |
| --- | --- | --- | --- |
| `POST` | `/uploads/image` | Upload an image to Cloudinary | No |

## Database

The API creates tables automatically on startup using `Base.metadata.create_all(bind=engine)` in `app/main.py`.

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

The backend authenticates users with JWT access tokens signed using the `SECRET_KEY` and `ALGORITHM` values from `app/core/config.py`.

Flow:

1. Client sends credentials to `/users/login` or `/users/login/oauth2`.
2. `login_user()` verifies the password and creates a JWT payload with `sub`, `email`, and `role`.
3. The token is returned in the response body as `access_token`.
4. `OAuth2PasswordBearer` reads the bearer token from the `Authorization` header.
5. `get_current_user()` decodes the token and loads the database user.
6. `require_role([...])` checks the user's role before allowing access to protected routes.

Available roles are defined in `app/core/enums.py`:

- `USER`
- `ADMIN`

## File / Image Upload

Image uploads are handled through Cloudinary.

- The upload helper is `app/modules/uploads/service.py`.
- `app/core/cloudinary.py` configures Cloudinary from environment values.
- Product creation and user avatar updates both call the same upload helper.
- The returned payload includes:
  - `public_id`
  - `url`

This covers profile avatar uploads and product cover uploads.

## Deployment

### Docker Compose

The repo includes a compose stack at the root:\n
```yaml
services:
  mysql:
  backend:
  frontend:
```

It provisions:

- a MySQL 8 container,
- the FastAPI backend container built from `app/Dockerfile`,
- the frontend container built from `shop-fe/Dockerfile`.

Run from the project root:

```bash
cd shop
docker compose up --build
```

### Backend container

The backend image uses:

```dockerfile
FROM python:3.14-slim
WORKDIR /workspace
COPY app/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## License

This project is licensed under the MIT License. The full license text is available in [app/LICENSE](LICENSE).