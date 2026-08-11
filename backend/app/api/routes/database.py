from fastapi import APIRouter
from sqlalchemy import text

from app.db.engine import engine

router = APIRouter(
    prefix="/api/v1/database",
    tags=["Database"],
)


@router.get("/health")
def database_health() -> dict[str, str]:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {
        "status": "ok",
        "database": "aegisgrid",
    }
