from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
import json
from datetime import datetime
import os

if os.path.exists("orders.json"):
    with open('orders.json') as file:
        orders = json.load(file)
else:
    with open('orders.json', "w") as file:
        json.dump("[]", file)
app = FastAPI()
origins = [
    "http://localhost/",
    "http://localhost:8080/",
    "https://localhost.tiangolo.com/",
    "http://127.0.0.1:5500/",
    "https://arnevangheel.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Order(BaseModel):
    first_name: str
    last_name: str


@app.post("/order")
async def create_order(item: Order):
    orderid = len(orders)
    order = {"OrderId": orderid}
    order["orderedAt"] = datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")
    order.update(item.dict())
    orders.append(order)
    with open("orders.json", "w") as file:
        json.dump(orders, file)
    return orders[orderid]

@app.get("/orders/{id}")
async def get_order(id: int):
    return orders[id]

@app.get("/all_orders")
async def get_allorder():
    return orders
