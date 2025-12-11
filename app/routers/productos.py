from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.models import Producto
from database.deps import get_db
from schemas.producto import ProductoIn, ProductoOut, ProductoUpdate



router = APIRouter(
    prefix='/productos',
    tags=["Productos"]
)

@router.post('/', response_model=ProductoOut, status_code=201)
def crearProducto(producto: ProductoIn, db: Session = Depends(get_db)):

    nuevoProducto = Producto(
        nombre = producto.nombre,
        precio = producto.precio,
        stock_inicial = producto.stock_inicial
    )

    db.add(nuevoProducto)
    db.commit()
    db.refresh(nuevoProducto)

    return nuevoProducto

@router.get('/', response_model=list[ProductoOut])
def obtenerProductos(db: Session = Depends(get_db)):
    productos = db.query(Producto).all()
    return productos

@router.get('/{id}', response_model=ProductoOut)
def ObtenerProducto(id: int, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == id).first()

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.put('/{id}', response_model=ProductoOut)
def actualizarProducto(id: int, datos: ProductoUpdate, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == id).first()

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    for key, value in datos.dict(exclude_unset=True).items():
        setattr(producto, key, value)

    db.commit()
    db.refresh(producto)
    return producto

@router.delete("/{id}", status_code=204)
def eliminarProducto(id: int, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == id).first()

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    db.delete(producto)
    db.commit()
    return