from sqlalchemy import Column, Integer, String, Float
from database.engine import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    precio = Column(Float, nullable=False)
    stock_inicial = Column(Integer, nullable=False)