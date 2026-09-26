from fastapi import APIRouter, FastAPI
from app.schemas.expense import CreateExpense, ExpenseResponse, ExpenseList
from app.services.expense import create_expense


router = APIRouter()


@router.post(
    "/expenses"
)
async def create_expense(
    expense_create : CreateExpense,
    db: Session = Depends(get_db),
) -> ExpenseResponse:

    data = await create_expense(db, expense_create)
    return data


@router.get(
    "/expenses"
)
async def get_expenses(
    db: Session = Depends(get_db),
) -> ExpenseList:

    data = await get_all_expenses(db)
    return data

@router.get(
    "/expenses/month/{year}/{month}"
)
async def get_expenses(
    db: Session = Depends(get_db),
) -> ExpenseList:

    data = await get_all_expenses(db)
    return data




