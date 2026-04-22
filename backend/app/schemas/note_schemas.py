from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NoteRequest(BaseModel):
    title: str
    content: str

class NoteResponse(BaseModel):
    id: str
    title: str
    content: str
    summary: Optional[str] = None
    created_at: datetime