from fastapi import FastAPI
from database import engine, Base
from login_management import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Login Management")

app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"message": "FastAPI Login Management API"}

