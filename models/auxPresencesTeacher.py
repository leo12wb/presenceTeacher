from pydantic import BaseModel
from typing import Optional

class AuxPresencesTeacher(BaseModel):
    id: Optional[int] = None  # Campo id opcional
    teacherId: Optional[int] = None
    presencesTeacherId: Optional[int] = None
    status: str 
