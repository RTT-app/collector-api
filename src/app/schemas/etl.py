from pydantic import BaseModel

class ExtractDTO(BaseModel):
    id: str

class TransformDTO(BaseModel):
    id: str

class GetDataDTO(BaseModel):
    json_data: str