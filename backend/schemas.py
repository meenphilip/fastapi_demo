from pydantic import BaseModel


# Pydantic Product model
class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int


