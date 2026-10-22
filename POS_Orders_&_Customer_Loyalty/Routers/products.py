from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from decimal import Decimal
from dayabase import get_db
from Schemas.products import CreateProduct,SearchProductsResponse,CreateProductResponse
from Services.products import ProductServices

router = APIRouter(
 prefix="/api/v1/products",
 tags=["Products"]
)
@router.post("", response_model=CreateProductResponse, status_code=201)
def create_product(data: CreateProduct,db: Session = Depends(get_db)):
 return ProductServices.product_create(db, data.model_dump())
