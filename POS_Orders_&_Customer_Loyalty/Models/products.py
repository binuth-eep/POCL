from dayabase import  Base
from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, ForeignKey


class Products(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True)
    product_code = Column(String, unique=True )
    product_name = Column(String, nullable=False)
    unit_price = Column(DECIMAL, nullable=False )
    available_quantity = Column(Integer, nullable=False)
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey('categories.id'))





