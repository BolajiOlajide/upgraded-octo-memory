from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="Some weird ass server I don't need",
    description="Dang! The title should be the description."
)

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


"""
The command uvicorn main:app refers to:

main: the file main.py (the Python "module").
app: the object created inside of main.py with the line app = FastAPI().
--reload: make the server restart after code changes. Only do this for development.
"""
