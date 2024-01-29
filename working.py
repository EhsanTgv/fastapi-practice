from fastapi import FastAPI, Path

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
def get_item(item_id : int = Path(description="The ID of the item you'd like to view")):
    return inventory[item_id]
