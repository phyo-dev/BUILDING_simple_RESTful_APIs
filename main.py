from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    is_offer: Optional[bool] = None

## items dictionary can be assume as a database.
items = {
    1: {
        "name": "s-pen",
        "price": 45000,
        "is_offer": True
    },
    2: {
        "name": "mouse",
        "price": 15000,
        "is_offer": True
    },
}

@app.get('/')
async def root():
    return {"Hello":"Welcome from Phyo Pyae Sone Site"}

@app.get('/items/{item_id}')
async def read_item(item_id: int = Path(None, description="The ID of the item you want to view"), q: str = None):
    return items[item_id]

@app.get('/get-all-items')
async def read_item(q: str = None):
    return {"Items": items, "Items-count":len(items)}

@app.post('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    if item_id in items:
        return {"Error": "item already exit"}
    items[item_id] = item
    return items[item_id]
    
@app.put('/items/{item_id}')
async def update_item(item_id: int, item: UpdateItem):
    if item_id not in items:
        return {"Error": "Item does not exit"}
    if item.name != None:
        items[item_id]['name'] = item.name
    if item.price != None:
        items[item_id]['price'] = item.price
    if item.is_offer != None:
        items[item_id]['is_offer'] = item.is_offer
    
    return items[item_id]

@app.delete('/items/{item_id}')
async def delete_item(item_id: int):
    if item_id not in items:
        return {"Error": "Item does not exit"}
    del items[item_id]
    return {"Message": "Student deleted successfully"}