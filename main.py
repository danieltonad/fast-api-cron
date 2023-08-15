from fastapi import FastAPI, Query
import json
import Scheduler.app
app = FastAPI()



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


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[int] = None):
#     return {"item_id": item_id, "q": q}


