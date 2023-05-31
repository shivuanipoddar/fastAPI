from pydantic import BaseModel


class Car(BaseModel):
    name: str
    description: str
    model: str
    price: int
    company: str


