from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    perfil: str

class UserResponse(BaseModel):
    id: str
    nome: str
    email: str
    perfil: str
    ativo: bool

    class Config:
        from_attributes = True