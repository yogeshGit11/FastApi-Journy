from fastapi import FastAPI

app=FastAPI()

@app.get("/get/{id}")
async def get_stud(id:int):
    return {
        "msg":"Hey stud",
        "id":id
    }

@app.post("/add")
async def add_stud(student:dict):
    return {
        "msg":"Student added!!",
        "stud":student
    }

@app.put("/update/{id}")
async def update_stud(student:dict,id:int):
    return{
        "msg":f"Student with id={id} is updated!!",
        "stud":student
    }

@app.patch("/update_one/{id}")
async def update_single_stud(student:dict,id:int):
    return{
        "msg":f"Songle Student with id={id} is updated!!",
        "stud":student
    }

@app.delete("/delete_stud/{id}")
async def delete_stud(id:int):
    return{
        "msg":f"Student with id={id} is DEleted!!",
    }


#---------------------------------------
#path parameter predinfined value
from enum import Enum

class Category(Enum):
    marathi="marathi"
    gujrati="gujrati"
    english="english"

@app.get("/get-cat/{cat}")
def get_cat(cat:Category):
    if cat==Category.marathi:
        return {
            "msg":"Marathi cat found"
        }
    else:
        return{
            "msg":"another cat"
        }
    # return {
    #     "msg":"category Found!!!",
    #     "cat":cat
    # }


#-----------------------------------------------
#path convertor

@app.get("/get-path/{filepath:path}")
def get_path(filepath:str):
    return {
        "msg":f"file path is {filepath}"
    }
