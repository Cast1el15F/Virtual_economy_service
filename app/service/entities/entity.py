from datetime import datetime
from typing import Literal, Annotated
from pydantic import BaseModel, Field

class User(BaseModel):
    # id: int 
    username: Annotated[str, Field(max_length=50)]
    email: Annotated[str, Field(max_length=50)]
    balance: int = 0
    # created_at = datetime.now()

class Product(BaseModel):
    # id: int
    name: Annotated[str, Field(max_length=50)]
    description: Annotated[str, Field(max_length=500)]
    price: int = 0
    type: Literal["consumable", "permanent"]
    is_active: bool

class Inventory(BaseModel):
    # id: int
    user_id: int
    product_id: int
    quantity: int
    # purchased_at = datetime.now()

class Transaction(BaseModel):
    id: int
    user_id: int
    product_id: int
    amount: float
    status: Literal["pending", "completed", "failed"]
    # created_at = datetime.now()
