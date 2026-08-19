from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class SigmaRuleBase(BaseModel):
    title: str
    log_source: str
    detection: str
    severity: str


class SigmaRuleCreate(SigmaRuleBase):
    pass


class SigmaRuleResponse(SigmaRuleBase):
    id: UUID
    enabled: bool
    created_at: datetime

    model_config = {
        "from_attributes": True,
    }