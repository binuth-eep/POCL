from dayabase import  Base
from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, ForeignKey, DateTime


class Order(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True)
    customer_id =Column(Integer, ForeignKey('customer_id '))
    order_date_time =Column(DateTime, nullable=False)
    order_status = Column(String, nullable=False)
    total_amount = Column(DECIMAL(12,2), nullable=False)
    loyalty_points_earned = Column(DECIMAL(10,2), nullable=False)

