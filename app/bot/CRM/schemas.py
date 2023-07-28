from typing import List

from pydantic import BaseModel

# {
#     "id": product.product.id,
#     "name": product.product.name,
#     "count": product.count,
#     "options": product.options,
#     "summ": product.summ,
#     "wholesale_price": product.product.wholesale_price,
#     "retail_price": product.product.retail_price,
#     "discount": product.product.discount,
#     "articul": product.product.articul
# }
class ProductInOrderSchema(BaseModel):
    order_id: int | None
    id: int
    name: str
    count: int
    options: str | None
    summ: str
    wholesale_price: int
    retail_price: int
    discount: int
    articul: str | None

# {
#     "id": order.id,
#     "contacts": order.contacts,
#     "summ": order.summ,
#     "created_at": order.created_at.strftime("%m/%d/%Y, %H:%M:%S"),
#     "products": products_in_order
# }
class OrderSchema(BaseModel):
    id:int
    contacts: str
    summ: str
    created_at: str
    products: List[ProductInOrderSchema]




class ConsultationSchema(BaseModel):
    name: str
    contacts: str
    text: str