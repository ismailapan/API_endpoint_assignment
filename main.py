from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Product Information API")

db_params = {
    "host":os.getenv("DB_HOST"),
    "database":os.getenv("DB_NAME"),
    "user":os.getenv("DB_USER"),
    "password":os.getenv("DB_PASSWORD"),
    "port":os.getenv("DB_PORT")
}

def get_connect():
    return psycopg2.connect(**db_params)

@app.get("/")
def get_all_product():
    try:
        connect = get_connect()
        cursor = connect.cursor()

        cursor.execute("""
            Select * From products
        """)

        rows = cursor.fetchall()
        cursor.close()
        connect.close()

        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category":row[2],
                "price": row[3],
                "stock":row[4],
                "created_at": str(row[5])
            })

        return {"products": products}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
    
@app.post("/add_product")
def add_product(name: str, category: str, price: float, stock: int):

    try:
        connect = psycopg2.connect(**db_params)
        cursor = connect.cursor()

        cursor.execute(
            "Insert Into products(name, category, price, stock) Values (%s, %s, %s, %s);",
            (name, category, price, stock)
        )

        connect.commit()

        cursor.close()
        connect.close()

    except Exception as e:
        raise HTTPException(status_code=500, detail= str(e))
