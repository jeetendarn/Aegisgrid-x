from pydantic import BaseModel


class DeviceResponse(BaseModel):
    hostname: str
    device_type: str

    model_config = {
        "from_attributes": True
    }
