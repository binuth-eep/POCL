
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from Models.products import Products
from Repositories.products import ProductRepository
from Schemas.products import SearchProductsResponse,CreateProduct


class ProductServices:
    def __init__(self, Product_repo:ProductRepository):
        self.Product_repo = Product_repo



    def product_create(self,db: Session, data: dict):
        product_code = data["product_code"]
        existing =self.Product_repo.get_by_registration(db,product_code)
        if existing:
            raise HTTPException(
                status_code=409,
                detail="Registration number already exists"
            )
        try:
            return Products(db, data)
        except IntegrityError:
            db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Registration number already exists"
        )

    def product_search(self,db: Session, data: dict):
        product_code = data["product_code"]



