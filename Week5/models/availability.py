from sqlalchemy import Column, Integer, DateTime, Boolean, ForeignKey
from app.database import Base

class Availability(Base):
    __tablename__ = "availabilities"

    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    is_booked = Column(Boolean, default=False)