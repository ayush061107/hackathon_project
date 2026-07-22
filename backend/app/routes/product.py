from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas, auth

router = APIRouter(prefix="/products",tags=["Products"])

@router.post("/", response_model=schemas.ProductResponse, status_code = status.HTTP_201_CREATED)
def create_product(product : schemas.ProductCreate, current_user : models.User = Depends(auth.get_current_user),db : Session = Depends(get_db)):
    new_product = models.Product(
        name = product.name,
        brand= product.brand,
        category = product.category,
        price = product.price,
        rating= product.rating,
        ram= product.ram, 
        storage= product.storage,
        battery= product.battery,
        weight= product.weight
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get("/",
        response_model=list[schemas.ProductResponse])
def get_products(
    current_user : models.User = Depends(auth.get_current_user),
    db : Session = Depends(get_db)
):
    return db.query(models.Product).all()

@router.get(
    "/{product_id}",
    response_model=schemas.ProductResponse
)
def get_product(
    product_id :int,
    current_user: models.User = Depends(auth.get_current_user),
    db : Session = Depends(get_db)
):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product not found")
    return product
@router.put(
    "/{product_id}",
    response_model= schemas.ProductResponse
)
def update_product(
    product_id : int, 
    updated_product: schemas.ProductCreate,
    current_user : models.User = Depends(auth.get_current_user),
    db : Session = Depends(get_db)
):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product Not found")
    product.name=updated_product.name
    product.brand=updated_product.brand
    product.category=updated_product.category
    product.price=updated_product.price
    product.rating=updated_product.rating
    product.ram=updated_product.ram
    product.storage= updated_product.storage
    product.battery=updated_product.battery
    product.weight=updated_product.weight
    
    db.commit()
    db.refresh()
    
    return product

@router.delete("/{product_id}")
def delete_product(
    product_id : int,
    current_user : models.User=Depends(auth.get_current_user),
    db : Session = Depends(get_db)
):
    product= db.query(models.Product).filter(models.Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product not found")
    db.delete(product)
    db.commit()
    return {"message" : "Product deleted successfully!"}
