from pydantic import BaseModel



class ConsultationSchema(BaseModel):
    name: str
    contacts: str
    text: str