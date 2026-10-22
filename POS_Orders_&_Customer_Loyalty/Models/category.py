from dayabase import  Base
from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, ForeignKey

class Category(Base):
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True)
    category_code = Column(String, unique=True)
    category_name = Column(String, nullable=False)
    description = Column(String)
    active = Column(Boolean, default=True)