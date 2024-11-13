from fastapi import APIRouter, HTTPException, Query
from typing import List, Union, Optional
from models.presencesTeacher import PresencesTeacher
from models.auxPresencesTeacher import AuxPresencesTeacher
from repositories.presencesTeacher import (
    create as repoCreate,
    readAll as repoReadAll,
    readOne as repoReadOne,
    readAllTeacherActivities as repoReadAllTeacherActivities, 
    update as repoUpdate,
    delete as repoDelete,
)

router = APIRouter()
Request = Union[PresencesTeacher, AuxPresencesTeacher]

@router.post("/presencesTeacher", response_model=Request)
def create(body: Request):
    return repoCreate(body)

@router.get("/presencesTeacher", response_model=List[object])
def readAll(start_date: Optional[str] = Query(None), end_date: Optional[str] = Query(None)):
    if start_date and end_date:
       return repoReadAllTeacherActivities(start=start_date, end=end_date)
    else:
       return repoReadAll() 

@router.get("/presencesTeacher/{id}", response_model=object)
def read(id: int):
    res = repoReadOne(id)
    if res is None:
        raise HTTPException(status_code=404, detail="not found")
    return res

@router.put("/presencesTeacher/{id}", response_model=Request)
def update(id: int, body: Request):
    return repoUpdate(id, body)

@router.delete("/presencesTeacher/{id}")
def delete(id: int):
    repoDelete(id)
    return {"id": id}

