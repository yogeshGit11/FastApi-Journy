from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def hello():
    return {"MSG":"Jay Shree Ram"}