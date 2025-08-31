from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()


class Students(BaseModel):
    id: int = Field(title="Stud ID", description="Id of student")
    name: str = Field(title="Stud Name")
    city: str | None = Field(title="Stud city")



@app.get("/getstud")
def add_stud() -> Students:
    return {"id": 101, "name": "Rajaram", "city": "Mumbai"}
    # return {"id": 101, "name": "Rajaram"}
    # return {"id": 101, "name": "Rajaram","city":"Rampur","age":12}