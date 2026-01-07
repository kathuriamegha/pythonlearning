import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.availability import Availability
from app.models.appointment import Appointment
from app.schemas.appointment import AppointmentCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/book/{patient_id}")
def book(patient_id: int, data: AppointmentCreate, db: Session = Depends(get_db)):
    slot = db.query(Availability).filter(
        Availability.doctor_id == data.doctor_id,
        Availability.start_time <= data.appointment_time,
        Availability.end_time > data.appointment_time,
        Availability.is_booked == False
    ).first()

    if not slot:
        raise HTTPException(400, "Slot not available")

    slot.is_booked = True
    appointment = Appointment(
        doctor_id=data.doctor_id,
        patient_id=patient_id,
        appointment_time=data.appointment_time
    )
    db.add(appointment)
    db.commit()
    return {"message": "Appointment booked"}


@router.delete("/{appointment_id}")
def cancel_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = db.query(Appointment).filter(
        Appointment.id == appointment_id
    ).first()

    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    # Free availability slot
    slot = db.query(Availability).filter(
        Availability.doctor_id == appointment.doctor_id,
        Availability.start_time == appointment.appointment_time
    ).first()

    if slot:
        slot.is_booked = False

    db.delete(appointment)
    db.commit()

    return {"message": "Appointment cancelled"}


@router.get("/upcoming")
def upcoming_appointments(
    user_id: int,  # later extract from JWT
    db: Session = Depends(get_db)
):
    return (
        db.query(Appointment)
        .filter(
            Appointment.user_id == user_id,
            Appointment.appointment_time >= datetime.utcnow()
        )
        .all()
    )
