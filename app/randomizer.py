from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()
origins = [
    "http://localhost/",
    "http://localhost:8080/",
    "https://localhost.tiangolo.com/",
    "http://localhost:63342/",
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
orders = []

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
    return orders[orderid]

@app.get("/orders/{id}")
async def get_order(id: int):
    order = next((item for item in orders if item["OrderId"] == id), None)
    if order != None:
        return order
    else:
        raise HTTPException(status_code=404, detail="No order found with this ID")

@app.get("/all_orders")
async def get_allorder(user: str = None):
    if len(orders) < 0:
        raise HTTPException(status_code=404, detail="No orders found")
    else:
        if user is not None:
            list = []
            for i in orders:
                if i["first_name"] == user:
                    list.append(i)
            return list
        else:
            return orders
