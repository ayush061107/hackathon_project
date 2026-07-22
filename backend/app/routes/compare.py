from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas, auth

router = APIRouter(
    prefix="/compare",
    tags=["Comparison"]
)


# Create Comparison
@router.post(
    "/",
    response_model=schemas.ComparisonResponse,
    status_code=status.HTTP_201_CREATED
)
def create_comparison(
    comparison: schemas.ComparisonCreate,
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):

    new_comparison = models.Comparison(
        title=comparison.title,
        user_id=current_user.id
    )

    db.add(new_comparison)
    db.commit()
    db.refresh(new_comparison)

    return new_comparison


# Get All Comparisons of Logged-in User
@router.get(
    "/",
    response_model=list[schemas.ComparisonResponse]
)
def get_comparisons(
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):

    comparisons = (
        db.query(models.Comparison)
        .filter(models.Comparison.user_id == current_user.id)
        .all()
    )

    return comparisons


# Get Single Comparison
@router.get(
    "/{comparison_id}",
    response_model=schemas.ComparisonResponse
)
def get_comparison(
    comparison_id: int,
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):

    comparison = (
        db.query(models.Comparison)
        .filter(
            models.Comparison.id == comparison_id,
            models.Comparison.user_id == current_user.id
        )
        .first()
    )

    if comparison is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comparison not found"
        )

    return comparison


# Add Product to Comparison
@router.post(
    "/add-product",
    status_code=status.HTTP_201_CREATED
)
def add_product(
    data: schemas.ComparisonProductCreate,
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):

    comparison = (
        db.query(models.Comparison)
        .filter(
            models.Comparison.id == data.comparison_id,
            models.Comparison.user_id == current_user.id
        )
        .first()
    )

    if comparison is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comparison not found"
        )

    product = (
        db.query(models.Product)
        .filter(models.Product.id == data.product_id)
        .first()
    )

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    exists = (
        db.query(models.ComparisonProduct)
        .filter(
            models.ComparisonProduct.comparison_id == data.comparison_id,
            models.ComparisonProduct.product_id == data.product_id
        )
        .first()
    )

    if exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product already added to comparison"
        )

    new_link = models.ComparisonProduct(
        comparison_id=data.comparison_id,
        product_id=data.product_id
    )

    db.add(new_link)
    db.commit()

    return {
        "message": "Product added successfully"
    }


# Delete Comparison
@router.delete("/{comparison_id}")
def delete_comparison(
    comparison_id: int,
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):

    comparison = (
        db.query(models.Comparison)
        .filter(
            models.Comparison.id == comparison_id,
            models.Comparison.user_id == current_user.id
        )
        .first()
    )

    if comparison is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comparison not found"
        )

    db.query(models.ComparisonProduct).filter(
        models.ComparisonProduct.comparison_id == comparison_id
    ).delete()

    db.delete(comparison)
    db.commit()

    return {
        "message": "Comparison deleted successfully"
    }