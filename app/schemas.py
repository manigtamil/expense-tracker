from pydantic import BaseModel

class ExpenseCreate(BaseModel):
    amount: float
    category: str
    description: str

class ExpenseResponse(ExpenseCreate):
    id: int

    class Config:
        orm_mode = True