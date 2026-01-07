from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.availability import Availability
from app.models.doctor import Doctor
from app.models.user import User
from app.schemas.doctor import DoctorCreate, DoctorResponse
from app.schemas.user import UserRole

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/profile/{user_id}")
def create_profile(user_id: int, data: DoctorCreate, db: Session = Depends(get_db)):
    user = db.query(User).get(user_id)
    if not user or user.role != "Doctor":
        raise HTTPException(400, "Invalid doctor user")

    doctor = Doctor(user_id=user_id, specialization=data.specialization, experience=data.experience)
    db.add(doctor)
    db.commit()
    return {"message": "Doctor profile created"}



@router.get("/{doctor_id}/availability")
def get_doctor_availability(
    doctor_id: int,
    db: Session = Depends(get_db)
):
    return (
        db.query(Availability)
        .filter(Availability.doctor_id == doctor_id)
        .all()
    )

@router.get("/", response_model=List[DoctorResponse])
def list_doctors(db: Session = Depends(get_db)):
    doctors = (
        db.query(User)
        .filter(User.role == UserRole.DOCTOR)
        .all()
    )
    return doctors
