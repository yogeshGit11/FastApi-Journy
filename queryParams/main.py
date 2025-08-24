from fastapi import FastAPI, status, Query

app = FastAPI()

# # single Query parameter (http://127.0.0.1:8000/stud?name=gota)
# @app.get("/stud")
# def get_stud(name:str):
#     return{
#         "Msg":"Student Found!!",
#         "Name":name
#     }

# # mutiple Query parameter (http://127.0.0.1:8000/stud?name=gota&roll=49)
# @app.get("/stud")
# def get_stud(name:str,roll:int):
#     return{
#         "Msg":"Student Found!!",
#         "Name":name,
#         "Roll":roll
#     }


# # Query parameter default parameter (http://127.0.0.1:8000/stud?name=nitin)
# @app.get("/stud")
# def get_stud(name: str, roll: int = 99):
#     return {"Msg": "Student Found!!", "Name": name, "Roll": roll}


# # Query params with optional val (http://127.0.0.1:8000/stud?name=gota)
# @app.get("/stud")
# def get_stud(name: str, roll: int | None = None):
#     return {"Msg": "Student Found!!", "Name": name, "Roll": roll}


# # Query params with path params (http://127.0.0.1:8000/stud/367?name=gota&roll=28)
# @app.get("/stud/{id}",status_code=status.HTTP_201_CREATED)
# def get_stud(id: int, name: str, roll: int | None = None):
#     return {"Msg": "Student Found!!", "Name": name, "Roll": roll, "ID": id}


# use fo anottion and Query()
from typing import Annotated


@app.get("/get")
def get_stud(name: Annotated[str | None, Query(min_length=3)] = None):
    return {"Msg": "Student Found!!", "Name": name}
