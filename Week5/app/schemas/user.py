from pydantic import BaseModel, EmailStr
from enum import Enum

class UserRole(str, Enum):
    DOCTOR = "DOCTOR"
    PATIENT = "PATIENT"

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    role: UserRole
    name: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str
