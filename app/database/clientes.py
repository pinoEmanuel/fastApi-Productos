from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from database.engine import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    telefono = Column(String, nullable=True)

    productos = relationship(
        "Producto",
        back_populates="cliente",
        cascade="all, delete"
    )