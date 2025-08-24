from fastapi import FastAPI

app = FastAPI()

students = [
    {"id": 1, "name": "Alice Johnson", "city": "New York", "marks": 85},
    {"id": 2, "name": "Bob Smith", "city": "Los Angeles", "marks": 78},
    {"id": 3, "name": "Charlie Lee", "city": "Chicago", "marks": 92}
]

#CRUD Operation

#get all
@app.get("/students")
def get_all_student():
    return {
        "msg":"Student Data",
        "data":students
    }

#get one
@app.get("/students/{id}")
def get_all_student(id:int):
    for stud in students:
        if stud["id"]==id:
            return {
                "msg":"one student Data",
                "data":stud
            }

#add data
@app.post("/add")
def add_student(data:dict):
    students.append(data)
    return {
        "msg":"Student added!!!",
        "data":data
    }

#put/update data
@app.put("/update/{id}")
def update_student(id:int,data:dict):
    for index,stud in enumerate(students):
        if stud["id"]==id:
            students[index]=data
            return {
                "msg":"student updated!!!",
                "data":data
            }

#delete data
@app.delete("/delete/{id}")
def delete_student(id:int):
    for index,stud in enumerate(students):
        if stud["id"]==id:
            stud = students.pop(index)

            return{
                "msg":"stud deleted",
                "data":stud
            }