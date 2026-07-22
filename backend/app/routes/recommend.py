from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session 
from app.database import get_db
from app import auth, models, schemas
from app.utils.decision_engine import DecisionEngine

router = APIRouter(
    prefix="/recommend",
    tags=["Recommedation"]
)

@router.post("/{comparison_id}")
def recommend_product(
    comparison_id : int,
    priorities: schemas.PriorityWeights,
    current_user: models.User=Depends(auth.get_current_user),
    db : Session = Depends(auth.get_current_user)
):
    comparison = db.query(models.Comparison).filter(models.Comparison.id == comparison_id).first()
    if comparison is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comparison not found")
    comparison_products=(
        db.query(models.ComparisonProduct)
        .filter(models.ComparisonProduct.comparison_id == comparison_id).all
    )
    if len(comparison_products)<2:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Add atleast two products for comparison")
    products=[]
    for item in comparison_products:
        product = db.query(models.Product).filter(models.Product.id == item.product_id).first()
        if product:
            products.append(product)
    engine = DecisionEngine(products,priorities)
    result= engine.get_result()
    return result