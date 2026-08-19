from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.event import Event

router = APIRouter(
    prefix="/events",
    tags=["Events"],
)


@router.get("/")
def get_events(
    db: Annotated[Session, Depends(get_db)],
):
    return db.scalars(
        select(Event)
    ).all()