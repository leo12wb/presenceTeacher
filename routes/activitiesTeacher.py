from fastapi import APIRouter, HTTPException
from typing import List
from models.activitiesTeacher import ActivitiesTeacher
from repositories.presencesTeacher import (
    create as repoCreate,
    readAll as repoReadAll,
    readOne as repoReadOne,
    update as repoUpdate,
    delete as repoDelete,
)

router = APIRouter()
Request = ActivitiesTeacher

@router.post("/activitiesTeacher", response_model=Request)
def create(body: Request):
    return repoCreate(body)

@router.get("/activitiesTeacher", response_model=List[object])
def readAll():
    return repoReadAll()

@router.get("/activitiesTeacher/{id}", response_model=object)
def read(id: int):
    res = repoReadOne(id)
    if res is None:
        raise HTTPException(status_code=404, detail="not found")
    return res

@router.put("/activitiesTeacher/{id}", response_model=Request)
def update(id: int, body: Request):
    return repoUpdate(id, body)

@router.delete("/activitiesTeacher/{id}")
def delete(id: int):
    repoDelete(id)
    return {"id": id}

