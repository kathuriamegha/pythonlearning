from fastapi import FastAPI
from app.database import engine, Base
from app.router import auth, doctor, availability, appointment

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Doctor Appointment API")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(doctor.router, prefix="/doctor", tags=["Doctor"])
app.include_router(availability.router, prefix="/availability", tags=["Availability"])
app.include_router(appointment.router, prefix="/appointments", tags=["Appointments"])
