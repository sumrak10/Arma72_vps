import pydantic

class OrderSchema(pydantic.BaseModel):
    name: str
    summ: int