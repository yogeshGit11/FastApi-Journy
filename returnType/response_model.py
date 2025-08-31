from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Any

app = FastAPI()


class Students(BaseModel):
    id: int = Field(title="Stud ID", description="Id of student")
    name: str = Field(title="Stud Name")
    city: str | None = Field(title="Stud city")



@app.get("/getstud",response_model=Students)
def add_stud():
    return {"id": 101, "name": "Rajaram", "city": "Mumbai"}
    # return {"id": 101, "name": "Rajaram"}
    # return {"id": 101, "name": "Rajaram","city":"Rampur","age":12}