from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class EventBase(BaseModel):
    event_type: str
    source: str
    severity: str
    message: str


class EventCreate(EventBase):
    pass


class EventResponse(EventBase):
    id: UUID
    created_at: datetime

    model_config = {
        "from_attributes": True,
    }