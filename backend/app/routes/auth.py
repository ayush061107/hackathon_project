from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas, auth

router = APIRouter(prefix="",tags=["Authentication"])

@router.post("/register", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def register(user : schemas.UserCreate, db : Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email Already registered")
    new_user = models.User(
        name=user.name,
        email=user.email,
        password=auth.hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

@router.post("/login", response_model = schemas.Token)
def login(user : schemas.UserLogin, db : Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.user.email == user.email).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credential")
    if not auth.verify_password(user.password,db_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= "Invalid Credentials")
    access_token = auth.create_access_token(data={"user_id":db_user.id})
    return {"access_token": access_token,"token_type": "bearer"}
    