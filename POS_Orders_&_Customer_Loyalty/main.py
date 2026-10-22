
from fastapi import FastAPI
from dayabase import Base, engine
from Models.products import Products
from Routers.products import router as ProductRouter

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Product List API")

app.include_router(ProductRouter.router)
@app.get("/")
def home():
 return {"message": "Vehicle Inventory API is running"}


