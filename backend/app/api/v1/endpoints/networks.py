from sqlalchemy import select
from fastapi import APIRouter

from app.db.engine import SessionLocal
from app.models.network import Network

router = APIRouter()


@router.get("/networks")
def get_networks():
    with SessionLocal() as session:
        return session.scalars(
            select(Network)
        ).all()
