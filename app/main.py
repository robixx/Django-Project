

from fastapi import FastAPI, APIRouter

from app.core.database import Base, engine
from app.routers import user_router
# Create tables if they don't exist
Base.metadata.create_all(bind=engine)


app = FastAPI(title="Test API")

# Include the router from user_router.py
app.include_router(user_router.router)