from app.core.database import SessionLocal

def get_db():
    db = SessionLocal()

    try:
        yield db #pause function, return db for FastAPI to use
    finally:
        db.close()