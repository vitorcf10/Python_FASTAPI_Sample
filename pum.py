from fastapi import FastAPI, Path, Query, HTTPException, status
from pydantic import BaseModel


app =  FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: str = None

class updateItem(BaseModel):
    name: str = None
    price: float =  None
    brand: str = None

inventory = {}

""" 
inventory = {
    1:{
        "name": "Milk",
        "price": 3.99,
        "brand": "Xando"
    }
}
"""

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description = "The id of the item you would like to view.", gt = 0)):
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name: str = None, ):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    #raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)
    raise  HTTPException(status_code = 404, detail = "Item name not found.")
    
"""
@app.get("/get-by-name/{item_id}")
def get_item(*,item_id: int, name: str = None, test:int):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data": "Not found"}    
"""

@app.post("/create_item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise  HTTPException(status_code = 400, detail = "Item ID already exists.")
    inventory[item_id] = item   
    #inventory[item_id] = {"name": item.name, "brand": item.brand, "price": item.price}    
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: updateItem):
    if item_id not in inventory:
        raise  HTTPException(status_code = 404, detail = "Item ID does not exist.")
    if item.name != None:
        inventory[item_id].name = item.name
    if item.price != None:
        inventory[item_id].price = item.price
    if item.brand != None:
        inventory[item_id].brand = item.brand
    
    return inventory[item_id]

@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int):
    if item_id not in inventory:
        raise  HTTPException(status_code = 404, detail = "Item ID does not exist.")
    del inventory[item_id]
    return{"Success": "Item deleted!"}
#Methods for endpoints: GET, POST, PUT, DELETE
#GET: Endpoint returns info, gets something for you.
#POST: Send info to the post endpoint or creating(post) data 
#PUT: Update something that is already in the data base
#DELETE: Delete information from data base.

"""
@app.get("/")
def home():
    return{"CHUPA MIN"}

@app.get("/about")
def about():
    return{"About"}
"""