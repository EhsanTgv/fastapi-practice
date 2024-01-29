from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


@app.get("/")
def home():
    return {"Data": "Test"}


inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Regular"
    }
}


@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description="The ID of the item you'd like to view", gt=0)):
    return inventory[item_id]


@app.get("/get-by-name")
def get_item(*, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data", "Not found"}


@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error", "Item ID already exists"}

    inventory[item_id] = item
    return inventory[item_id]
