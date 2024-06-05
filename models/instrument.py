from pydantic import BaseModel
from typing import Optional


class Instrument(BaseModel):
    id: int
    name: str
    category: str
    description: Optional[str] = None

