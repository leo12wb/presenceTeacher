from pydantic import BaseModel
from datetime import date, time
from typing import Optional

class PresencesTeacher(BaseModel):
    id: Optional[int] = None  # Campo id opcional
    _date: date = None
    _status: str
    start_hour: Optional[time] = None
    end_hour: Optional[time] = None
    status: str 
