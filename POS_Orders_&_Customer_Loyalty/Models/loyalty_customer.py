from dayabase import  Base
from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, ForeignKey,DateTime


class LoyaltyCustomer(Base):
    __tablename__ = 'loyalty_customer'
    customer_id = Column(Integer, primary_key=True )
    mobile_number = Column(Integer, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    loyalty_points = Column(Integer, nullable=False)
    registered_at = Column(DateTime, nullable=False)

