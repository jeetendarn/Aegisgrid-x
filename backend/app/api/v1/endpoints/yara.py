from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.yara_rule import YaraRule

router = APIRouter(
    prefix="/yara",
    tags=["YARA Rules"],
)


@router.get("/")
def get_yara_rules(
    db: Annotated[Session, Depends(get_db)],
):
    return db.scalars(
        select(YaraRule)
    ).all()