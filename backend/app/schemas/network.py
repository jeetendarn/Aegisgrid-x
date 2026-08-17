from pydantic import BaseModel


class NetworkResponse(BaseModel):
    name: str
    cidr: str

    model_config = {
        "from_attributes": True
    }
