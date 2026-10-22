from sqlalchemy.orm import Session
from sqlalchemy import func
from Models.products import Products

class ProductRepository:

 def get_by_registration(db: Session, product_code: str):
  return db.query(Products).filter(func.lower(Products.product_code)== product_code.lower()).first()


 def search_products(db: Session,product_id=None,product_name=None,product_code=None,active=True):

  query = db.query(Products)
  if product_id:
   query = query.filter(Products.product_id.ilike(f"%{product_id}%"))
  if product_name:
   query = query.filter(Products.product_name.ilike(f"%{product_name}%"))
  if product_code:
    query = query.filter(Products.product_code.ilike(f"%{product_code}%"))
  if active:
   query = query.filter(Products.active == active)

  return query.all()