from pydantic import BaseModel

class FileResponse(BaseModel):
    id: str
    url: str