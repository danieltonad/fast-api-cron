from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Annotated
import json

app = FastAPI()


class Item(BaseModel):
    name: str
    descripton: Annotated[str | None, Query(max_length=50)] = None
    price: float
    tax: float | None = None




@app.get("/")
def read_root():
    
    return {'data': 'success'}

@app.get("/data-type/{data}")
def read_root(data: int):
    
    return {'data': f'{data}'}

@app.get("/custom-test")
async def custom_test():
    f = open('./Storage/jobberman.json')
    data = json.load(f)
    f.close()
    return data

@app.post("/post-test")
async def post_param(item: Item):
    return item


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[int] = None):
#     return {"item_id": item_id, "q": q}


