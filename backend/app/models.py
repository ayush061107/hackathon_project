from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(260), nullable=False)

    comparisons = relationship(
        "Comparison",
        back_populates="user"
    )


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    brand = Column(String(100))
    category = Column(String(50))

    price = Column(Float)
    rating = Column(Float)

    ram = Column(Integer)
    storage = Column(Float)
    battery = Column(Integer)
    weight = Column(Float)

    comparison_products = relationship(
        "ComparisonProduct",
        back_populates="product"
    )


class Comparison(Base):
    __tablename__ = "comparisons"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    user = relationship(
        "User",
        back_populates="comparisons"
    )

    products = relationship(
        "ComparisonProduct",
        back_populates="comparison"
    )


class ComparisonProduct(Base):
    __tablename__ = "comparison_products"

    id = Column(Integer, primary_key=True, index=True)

    comparison_id = Column(
        Integer,
        ForeignKey("comparisons.id")
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id")
    )

    comparison = relationship(
        "Comparison",
        back_populates="products"
    )

    product = relationship(
        "Product",
        back_populates="comparison_products"
    )