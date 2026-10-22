from pydantic import BaseModel, Field
from typing import Optional



class SearchProductsResponse(BaseModel):
    Product_id: int = Field()
    Product_code: str = Field()
    Product_name: str = Field()
    Customer_id: int = Field()
    Customer_name: str = Field()
    unit_price: float = Field()
    available_quantity: int = Field()
    active: bool = Field()




class CreateProduct(BaseModel):

    # Product_code: str = Field()
    Product_name: str = Field()
    unit_price: float = Field()
    available_quantity: int = Field()
    active: bool = Field()
    category_id: int = Field()

class CreateProductResponse(BaseModel):
    Product_id:int = Field()
    Product_code: str = Field()
    Product_name: str = Field()
    unit_price:float = Field()
    available_quantity:int = Field()
    active:bool = Field()
    category_id:int = Field()


