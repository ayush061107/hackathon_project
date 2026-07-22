from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

database_URL = "mysql+pymysql://root:12345678@localhost/decisionflow_db"

engine = create_engine(
    database_URL,
    echo=False
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()   # <-- FIXED

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        