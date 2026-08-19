from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.threat_intelligence import ThreatIntelligence

router = APIRouter(
    prefix="/threat-intelligence",
    tags=["Threat Intelligence"],
)


@router.get("/")
def get_threat_intelligence(
    db: Annotated[Session, Depends(get_db)],
):
    return db.scalars(
        select(ThreatIntelligence)
    ).all()