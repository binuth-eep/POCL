from sqlalchemy.orm import Session
from sqlalchemy import func
from Models.loyalty_customer import LoyaltyCustomer

def create_customer(db: Session, data: dict):
    customer = LoyaltyCustomer()
    customer = customer(**data)
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

