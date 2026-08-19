from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.sigma_rule import SigmaRule

router = APIRouter(
    prefix="/sigma",
    tags=["Sigma Rules"],
)


@router.get("/")
def get_sigma_rules(
    db: Annotated[Session, Depends(get_db)],
):
    return db.scalars(
        select(SigmaRule)
    ).all()