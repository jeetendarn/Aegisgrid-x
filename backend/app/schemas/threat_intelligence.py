from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ThreatIntelligenceBase(BaseModel):
    ioc_type: str
    ioc_value: str
    source: str
    confidence: str
    description: str


class ThreatIntelligenceCreate(ThreatIntelligenceBase):
    pass


class ThreatIntelligenceResponse(ThreatIntelligenceBase):
    id: UUID
    created_at: datetime

    model_config = {
        "from_attributes": True,
    }