from sqlalchemy import select
from fastapi import APIRouter

from app.db.engine import SessionLocal
from app.models.branch import Branch

router = APIRouter()


@router.get("/branches")
def get_branches():
    with SessionLocal() as session:
        return session.scalars(
            select(Branch)
        ).all()
