from pydantic import BaseModel, EmailStr
from app.models.enums import UserRole

class UserCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    perfil: UserRole


class UserResponse(BaseModel):
    id: str
    nome: str
    email: str
    perfil: str
    ativo: bool

    class Config:
        from_attributes = True