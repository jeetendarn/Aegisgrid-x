from sqlalchemy import select
from fastapi import APIRouter

from app.db.engine import SessionLocal
from app.models.device import Device

router = APIRouter()


@router.get("/devices")
def get_devices():
    with SessionLocal() as session:
        return session.scalars(
            select(Device)
        ).all()
