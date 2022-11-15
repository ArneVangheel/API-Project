from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
app = FastAPI()
origins = [
    "http://localhost/",
    "http://localhost:8080/",
    "https://localhost.tiangolo.com/",
    "http://127.0.0.1:5500/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=[""],
)

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
    orders[{"OrderId": orderid}] = item.dict()
    return orders[orderId]

@app.get("/orders")
async def get_orders():
    return {"orders": orders}
