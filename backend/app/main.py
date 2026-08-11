from fastapi import FastAPI

from app.api.routes.database import router as database_router
from app.api.routes.health import router as health_router
from app.api.routes.system import router as system_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    description=(
        "AI-Powered Zero-Trust Cyber Range "
        "& Enterprise Security Fabric"
    ),
    version="0.1.0",
)

app.include_router(health_router)
app.include_router(system_router)
app.include_router(database_router)
