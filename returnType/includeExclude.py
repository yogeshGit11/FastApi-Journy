from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

student_data = {
    "1": {"name": "Riya", "age": 33, "city": "Nashik"},
    "2": {"name": "Piya", "age": 45, "city": "Dhule"},
}


class Students(BaseModel):
    name: str = Field(title="Stud Name")
    age: int
    city: str | None = Field(title="Stud city")


# @app.get("/getstud/{id}", response_model=Students,response_model_exclude="name")
@app.get("/getstud/{id}", response_model=Students,response_model_include=["name","city"])
def add_stud(id: str):
    if student_data.get(id):
        return student_data.get(id, {})
