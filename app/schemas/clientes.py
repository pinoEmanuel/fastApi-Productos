from pydantic import BaseModel, EmailStr, Field
from schemas.producto import ProductoOut

class ClienteBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50)
    apellido: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    telefono: str | None = Field(None, min_length=8, max_length=20)

class ClienteCreate(ClienteBase):
    pass

class ClienteOut(ClienteBase):
    id: int
    productos: list[ProductoOut] = []

    class Config:
        orm_mode = True