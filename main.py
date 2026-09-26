from fastapi import FastAPI
from pydantic import BaseModel, Field
from routers import user

from core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
) 
app.include_router(user.router, prefix=settings.api_prefix) # include the user router with the api prefix

class Product(BaseModel):
    name: str
    price: float
    description: str = None # Optional field default is none

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/products")
async def get_products():
    return {"products": ["Product 1", "Product 2", "Product 3"]}

@app.put("/products/{product_id}")
async def update_product(product_id: int, product: Product):
    return {"product_name": product.name, "product_id": product_id}

@app.post("/products")
async def create_product(product: Product):
    return {
        "success": True,
        "data":product
    }

# query parameters
@app.get("/products/search")
async def search_products(name: str = None, min_price: float = None, max_price: float = None):
    return {
        "name": name,
        "min_price": min_price,
        "max_price": max_price
    }

# localhost:8000/products/search?name=Product%201&min_price=10&max_price=100