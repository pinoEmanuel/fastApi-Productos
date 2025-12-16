from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.clientes import Cliente
from database.deps import get_db
from schemas.clientes import ClienteCreate, ClienteOut
from schemas.producto import ProductoOut

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)

@router.post("/", response_model=ClienteOut, status_code=201)
def crearCliente(cliente: ClienteCreate, db: Session = Depends(get_db)):

    existente = db.query(Cliente).filter(Cliente.email == cliente.email).first()
    if existente:
        raise HTTPException(status_code=400, detail="Email ya registrado")
    
    nuevo = Cliente(**cliente.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return nuevo

@router.get("/", response_model=list[ClienteOut])
def obtenerClientes(db: Session = Depends(get_db)):
    return db.query(Cliente).all()

@router.get("/{cliente_id}/productos", response_model=list[ProductoOut])
def obtenerProductosDeCliente(cliente_id: int, db: Session = Depends(get_db)):

    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not cliente: 
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    return cliente.productos