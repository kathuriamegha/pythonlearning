from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.availability import Availability
from app.schemas.availability import AvailabilityCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_availability(data: AvailabilityCreate, db: Session = Depends(get_db)):
    slot = Availability(**data.dict())
    db.add(slot)
    db.commit()
    return {"message": "Availability added"}