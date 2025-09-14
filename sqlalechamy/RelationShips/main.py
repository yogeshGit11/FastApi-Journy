from fastapi import Depends, FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from schemas import UserSchema, PostSchema
from tables import User, Post
from db import SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# USER SERVICES---------------------------------------------------------------
@app.get("/get-users/", status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    all_user = db.query(User).all()
    if not all_user:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"detail": "No users found."}
        )
    else:
        return [
            {"id": user.id, "name": user.name, "age": user.age} for user in all_user
        ]


@app.post("/add-user/", status_code=status.HTTP_201_CREATED)
def add_user(user: UserSchema, db: Session = Depends(get_db)):
    user = User(name=user.name, age=user.age)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"Msg": "USER ADDED!!", "User": user}


@app.put("/update-user/{user_id}", status_code=status.HTTP_201_CREATED)
def update_user(user_id: int, user: UserSchema, db: Session = Depends(get_db)):
    old_user = db.query(User).filter(User.id == user_id).first()
    if not old_user:
        return JSONResponse(
            content={"Msg": "User not found to update"},
            status_code=status.HTTP_404_NOT_FOUND,
        )
    else:
        old_user.name = user.name
        old_user.age = user.age
        db.commit()
        db.refresh(old_user)
        return {"Msg": "USER Updated!!"}
    
@app.delete("/delete-user/{user_id}")
def delete_user(user_id:int,db:Session=Depends(get_db)):
    old_user=db.query(User).filter(User.id==user_id).first()
    if not old_user:
        return JSONResponse(
            content={"Msg": "User not found to Delete"},
            status_code=status.HTTP_404_NOT_FOUND,
        )
    else:
        db.delete(old_user)
        db.commit()
        return {"Msg": "USER Deleted!!","User":old_user}


# POST SERVICES-------------------------------------------------------------
@app.get("/get-post/", status_code=status.HTTP_200_OK)
def get_post(db: Session = Depends(get_db)):
    all_post = db.query(Post).all()
    if not all_post:
        return JSONResponse(
            content={"Msg": "Post not found yet!!"},
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return [
        {"id": post.id, "title": post.title, "writer": post.writer.name}
        for post in all_post
    ]


@app.post("/add-post/", status_code=status.HTTP_201_CREATED)
def add_post(post: PostSchema, db: Session = Depends(get_db)):
    post = Post(title=post.title, user_id=post.user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return {"Msg": "Post Addded!!", "Post": post}
