from pydantic import BaseModel
from typing import List

class ExpenseCreate(BaseModel):
    name: str
    amount: float
    category: str

class ExpenseResponse(BaseModel):
    id : int
    name : str
    amount: float
    status : str

class ExpenseList(BaseModel):
    data : List[]
