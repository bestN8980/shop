from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.modules.users.router import router as user_routers
from app.modules.users.admin_router import router as admin_user_routers
from app.modules.products.router import router as product_routers
from app.modules.categories.router import router as category_routers
from app.modules.carts.router import router as cart_routers
from app.modules.orders.router import router as order_routers
from app.core.database import Base, engine
from app.modules.uploads.router import router as upload_router


app = FastAPI(
    title="Mini E-commerce API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://shop-fe.netlify.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    import app.modules.users.model
    import app.modules.products.model
    import app.modules.carts.model
    import app.modules.categories.model
    import app.modules.orders.model
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {
        "message": "Mini E-commerce API"
    }

app.include_router(user_routers)
app.include_router(admin_user_routers)
app.include_router(product_routers)
app.include_router(category_routers)
app.include_router(cart_routers)
app.include_router(order_routers)
app.include_router(upload_router)   
