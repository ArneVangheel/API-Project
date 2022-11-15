from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Order(BaseModel):
    first_name: str
    last_name: str
    street: str
    addition: str | None = None
    zipcode: int
    city: str

@app.post("/order")
async def create_item(item: Order):
    number = len(cards)
    cards[number] = item.dict()
    return cards[number]

@app.get("/orders")
async def create_item():
    return cards
