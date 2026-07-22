from app.database import SessionLocal
from app.models import Product


db = SessionLocal()

# Don't insert again if products already exist
if db.query(Product).first():
    print("Products already exist. Skipping seeding.")
    db.close()
    exit()

products = [
    Product(
        name="HP Victus 15",
        brand="HP",
        category="Laptop",
        price=62999,
        rating=4.3,
        ram=16,
        storage=512,
        battery=70,
        weight=2.37
    ),
    Product(
        name="Lenovo LOQ",
        brand="Lenovo",
        category="Laptop",
        price=67999,
        rating=4.5,
        ram=16,
        storage=512,
        battery=60,
        weight=2.40
    ),
    Product(
        name="ASUS TUF A15",
        brand="ASUS",
        category="Laptop",
        price=71999,
        rating=4.4,
        ram=16,
        storage=512,
        battery=90,
        weight=2.30
    ),
    Product(
        name="Dell G15",
        brand="Dell",
        category="Laptop",
        price=74999,
        rating=4.2,
        ram=16,
        storage=512,
        battery=56,
        weight=2.50
    ),
    Product(
        name="iPhone 15",
        brand="Apple",
        category="Smartphone",
        price=69999,
        rating=4.7,
        ram=6,
        storage=128,
        battery=3349,
        weight=0.171
    ),
    Product(
        name="Samsung Galaxy S24",
        brand="Samsung",
        category="Smartphone",
        price=65999,
        rating=4.6,
        ram=8,
        storage=256,
        battery=4000,
        weight=0.167
    ),
    Product(
        name="OnePlus 12",
        brand="OnePlus",
        category="Smartphone",
        price=64999,
        rating=4.6,
        ram=12,
        storage=256,
        battery=5400,
        weight=0.220
    ),
    Product(
        name="Nothing Phone (2)",
        brand="Nothing",
        category="Smartphone",
        price=42999,
        rating=4.4,
        ram=12,
        storage=256,
        battery=4700,
        weight=0.201
    )
]

db.add_all(products)
db.commit()

print(f"Inserted {len(products)} demo products successfully!")

db.close()