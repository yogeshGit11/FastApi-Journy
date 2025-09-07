from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from typing import Optional

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def getform():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Student Form</title>
</head>
<body>

  <h2>User Information Form</h2>
  <form action="/submit" method="post">
    <label for="name">Name:</label><br>
    <input type="text" id="name" name="name" required><br><br>

    <label for="age">Age:</label><br>
    <input type="number" id="age" name="age" min="0" required><br><br>

    <label for="city">City:</label><br>
    <input type="text" id="city" name="city" required><br><br>

    <input type="submit" value="Submit">
  </form>

</body>
</html>
"""


@app.post("/submit")
def add_stud(
    name: str = Form(...),
    age: int = Form(...),
    city: Optional[str] = Form(None)
):
    # Manual validation
    if len(name) < 4:
        return {"error": "Name must be at least 4 characters long."}
    if age < 18:
        return {"error": "Age must be at least 18."}

    return {"name": name, "age": age, "city": city}
