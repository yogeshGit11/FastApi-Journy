from fastapi import FastAPI, status
from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum

app = FastAPI()


class Gender(Enum):
    male = "male"
    female = "female"


class Student(BaseModel):
    id: int
    name: str = Field(..., min_length=4)
    age: int = 12
    gen: Gender
    # alive: bool | None = None
    alive: Optional[bool] = None


class Course(BaseModel):
    id: int
    name: str
    period: str


students = [{"id": 1, "name": "Ram", "age": 87, "gen": "male", "alive": True}]


@app.get("/get-stud")
def get_students():
    return {"Msg": "All students", "students": students}


# @app.post("/add-stud", status_code=status.HTTP_201_CREATED)
# def add_student(new_stud: Student):
#     stud = new_stud.model_dump()
#     students.append(stud)
#     return {"Msg": "Student added successfully!!!", "New_stud": stud}


@app.post("/add-stud", status_code=status.HTTP_201_CREATED)
def add_student(new_stud: Student, course: Course):
    return {
        "Msg": "Student added successfully!!!",
        "New_stud": new_stud,
        "course": course,
    }
