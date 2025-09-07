from fastapi import FastAPI,HTTPException

app=FastAPI()

student={
    "ram":"Jay Shree Ram!!!",
    "krishna":"Jay Shree Krishna!!!",
}

@app.get("/stud/{id}")
def get_stud(id:str):
    if id not in student:
        raise HTTPException(status_code=404,detail="Student Not Found!!!")
    return student.get(id)