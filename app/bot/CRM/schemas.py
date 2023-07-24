from pydantic import BaseModel

class OrderSchema(BaseModel):
    id:int
    client_name: str
    contacts: str
    summ: int
    created_at: str

class ProductInOrderSchema(BaseModel):
    order_id: int
    product_id: int
    product_name: str
    count: int
    summ: int
    summ_type: str
    option_id: int
    option_value: str



class AppealSchema(BaseModel):
    name: str
    contacts: str
    text: str