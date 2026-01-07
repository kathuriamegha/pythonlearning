from pydantic import BaseModel, EmailStr


class DoctorCreate(BaseModel):
    specialization: str
    experience: int


class DoctorResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    experience: int
    specialization: str

    class Config:
        from_attributes = True