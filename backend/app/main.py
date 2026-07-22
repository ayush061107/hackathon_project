from fastapi import FastAPI
from app.database import Base, engine 
from app.routes import auth, product, compare, recommend

Base.metadata.create_all(bind=engine)

app=FastAPI(title="DecisionFlow API",version="1.0.0")

app.include_router(auth.router)
app.include_router(product.router)
app.include_router(compare.router)
app.include_router(recommend.router)

@app.get("/")
def root():
    return {"message" : "Welcome to DecisionFlow"}