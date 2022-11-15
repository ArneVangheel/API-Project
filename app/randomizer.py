from fastapi import FastAPI
from pydantic import BaseModel, Field
import json

app = FastAPI()
orders = {}
class Order(BaseModel):
    first_name: str
    last_name: str
    street: str
    addition: str | None = None
    zipcode: int
    city: str

@app.post("/order")
async def create_order(item: Order):
    orderid = len(orders)
    orders[orderid] = item.dict()
    return orders[orderid]

@app.get("/orders")
async def get_orders(id: int):
    return orders
