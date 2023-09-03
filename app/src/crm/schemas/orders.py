from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel



class ProductSchema(BaseModel):
    id: int
    name: str
    count: int
    options: Optional[str]
    summ: str
    wholesale_price: Optional[int]
    retail_price: Optional[int]
    discount: int
    articul: Optional[str]

class OrderSchema(BaseModel):
    id: int
    contacts: str
    summ: str
    created_at: str
    products: List[ProductSchema]

#     class Config:
#         json_encoders = {
#             # custom output conversion for datetime
#             datetime: convert_datetime
#         }


# #utils
# def convert_datetime(datetime: datetime)