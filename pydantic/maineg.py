from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Subjects(BaseModel):
    name: str
    mark: int


class Student(BaseModel):
    name: str = Field(
        title="student name",
        description="Name of the student here",
        min_length=3,
        max_length=10,
    )
    age: int = Field(title="student age", description="Age of the student here", gt=18)
    married: bool = Field(default=False, title="is student married")
    subject: list[Subjects] = Field(
        title="subjcts", description="subjects and marks of student"
    )


students = []

@app.get("/get-stud")
def get_students():
    return {"Msg": "All students", "students": students}


@app.post("/add-stud")
def add_stud(stud: Student):
    students.append(stud.model_dump())
    return {"Msg": "Student added!!", "student": stud}
