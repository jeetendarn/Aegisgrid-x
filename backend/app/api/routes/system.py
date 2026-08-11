from fastapi import APIRouter

from app.core.config import settings

router = APIRouter(
    prefix="/api/v1/system",
    tags=["System"],
)


@router.get("/info")
def system_info() -> dict[str, str | bool]:
    return {
        "application": settings.app_name,
        "environment": settings.app_env,
        "debug": settings.app_debug,
        "version": "0.1.0",
    }


@router.get("/status")
def system_status() -> dict[str, str]:
    return {
        "status": "operational",
    }
