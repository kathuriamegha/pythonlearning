from pydantic import BaseModel
from datetime import datetime

class AvailabilityCreate(BaseModel):
    doctor_id: int
    start_time: datetime
    end_time: datetime