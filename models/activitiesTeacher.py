from pydantic import BaseModel
from typing import Optional

class ActivitiesTeacher(BaseModel):
    id: Optional[int] = None  # Campo id opcional
    abreviation: str = None
    _description: str
    status: str 
