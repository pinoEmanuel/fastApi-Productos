from fastapi import FastAPI
from routers import productos
from database.engine import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(productos.router)