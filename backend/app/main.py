from fastapi import FastAPI

from app.api.routes.database import router as database_router
from app.api.routes.health import router as health_router
from app.api.routes.system import router as system_router
from app.core.config import settings
from app.api.v1.endpoints.branches import router as branch_router
from app.api.v1.endpoints.networks import router as network_router
from app.api.v1.endpoints.devices import router as device_router
from app.api.v1.endpoints.mitre import router as mitre_router
from app.api.v1.endpoints.sigma import router as sigma_router
from app.api.v1.endpoints.yara import router as yara_router
from app.api.v1.endpoints.threat_intelligence import (
    router as threat_intelligence_router,
)
from app.api.v1.endpoints.events import router as events_router

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
app.include_router(
    branch_router,
    prefix="/api/v1",
    tags=["Branches"],
)

app.include_router(
    network_router,
    prefix="/api/v1",
    tags=["Networks"],
)

app.include_router(
    device_router,
    prefix="/api/v1",
    tags=["Devices"],
)

app.include_router(mitre_router)
app.include_router(sigma_router)
app.include_router(yara_router)

app.include_router(threat_intelligence_router)

app.include_router(events_router)
