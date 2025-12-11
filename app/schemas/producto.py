from pydantic import BaseModel, Field

class ProductoBase(BaseModel):
    nombre : str
    precio : float
    stock_inicial : int

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    nombre: str
    precio: float
    stock_inicial: int

class ProductoIn(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=50)
    precio: float = Field(..., gt=0)
    stock_inicial: int = Field(..., ge=0)

class ProductoOut(BaseModel):
    id: int
    
    class Config:
        orm_mode = True