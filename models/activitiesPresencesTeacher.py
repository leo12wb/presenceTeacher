from pydantic import BaseModel
from typing import Optional

class ActivitiesPresencesTeacher(BaseModel):
    id: Optional[int] = None  # Campo id opcional
    presencesTeacherId: Optional[int] = None
    activitiespresencesTeacherId: Optional[int] = None
    status: str 
