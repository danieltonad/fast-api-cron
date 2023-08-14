from pydantic import BaseModel
import datetime

order_json = {
    'item_id' : '123',
    'created_date' : '2023-06-14',
    'page_visited' : [1,2,'3'],
    'price' : '312.3'
}

class Order(BaseModel):
    item_id: int
    created_date: datetime.datetime
    page_visited: list
    price: float