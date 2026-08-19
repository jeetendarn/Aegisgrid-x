from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.mitre_technique import MitreTechnique

router = APIRouter(
    prefix="/mitre",
    tags=["MITRE ATT&CK"],
)


@router.get("/")
def get_techniques(
    db: Annotated[Session, Depends(get_db)],
):
    return db.scalars(
        select(MitreTechnique)
    ).all()