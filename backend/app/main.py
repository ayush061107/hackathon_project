from fastapi import FastAPI
from app.database import Base, engine 
from app.routes import auth, product, compare, recommend
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app=FastAPI(title="DecisionFlow API",version="1.0.0")

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(product.router)
app.include_router(compare.router)
app.include_router(recommend.router)

@app.get("/")
def root():
    return {"message" : "Welcome to DecisionFlow"}