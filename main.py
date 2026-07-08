from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API Endpoint")

class Product(BaseModel):
    id: int
    name: str
    price: float

products_db: list[Product] = [
    Product(id= 1, name= "Laptop", price= 50.0),
    Product(id= 2, name= "Mouse", price= 38.5),
    Product(id= 3, name= "Keyboard", price= 25.7),

]

@app.get("/")
def get_all_products():
    return products_db

@app.get("/product/{product_id}")
def get_product(product_id : int):
    for product in products_db:
        if product.id == product_id:
            return product
        raise HTTPException(status_code=404, detail="Not Found")