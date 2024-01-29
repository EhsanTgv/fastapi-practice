from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()


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
