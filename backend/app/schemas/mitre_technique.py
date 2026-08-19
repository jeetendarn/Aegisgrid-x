from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class MitreTechniqueBase(BaseModel):
    technique_id: str
    name: str
    tactic: str
    description: str
    platform: str


class MitreTechniqueCreate(MitreTechniqueBase):
    pass


class MitreTechniqueResponse(MitreTechniqueBase):
    id: UUID
    created_at: datetime

    model_config = {
        "from_attributes": True,
    }