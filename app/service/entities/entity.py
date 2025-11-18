from datetime import datetime
from typing import Literal
from pydantic import BaseModel

class User(BaseModel):
    id: int 
    username: str
    email: str
    balance: int
    created_at = datetime.now()

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: int
    type: Literal["consumable", "permanent"]
    is_active: bool

class Inventory(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    purchased_at = datetime.now()

class Transaction(BaseModel):
    id: int
    user_id: int
    product_id: int
    amount: int
    status: Literal["pending", "completed", "failed"]
    created_at = datetime.now()
