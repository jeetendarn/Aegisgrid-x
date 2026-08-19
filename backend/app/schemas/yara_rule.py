from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class YaraRuleBase(BaseModel):
    name: str
    rule: str
    category: str
    severity: str


class YaraRuleCreate(YaraRuleBase):
    pass


class YaraRuleResponse(YaraRuleBase):
    id: UUID
    enabled: bool
    created_at: datetime

    model_config = {
        "from_attributes": True,
    }