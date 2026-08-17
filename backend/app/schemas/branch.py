from pydantic import BaseModel


class BranchResponse(BaseModel):
    name: str
    code: str
    location: str

    model_config = {
        "from_attributes": True
    }
