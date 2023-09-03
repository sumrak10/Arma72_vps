from typing import List
from datetime import datetime

from pydantic import BaseModel



class ProductSchema(BaseModel):
    id: int
    name: str
    count: int
    options: str
    summ: str
    wholesale_price: int
    retail_price: int
    discount: int
    articul: str

class OrderSchema(BaseModel):
    id: int
    contacts: str
    summ: int
    created_at: datetime
    products: List[ProductSchema]

#     class Config:
#         json_encoders = {
#             # custom output conversion for datetime
#             datetime: convert_datetime
#         }


# #utils
# def convert_datetime(datetime: datetime)