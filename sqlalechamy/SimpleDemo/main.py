from fastapi import FastAPI, Depends
from db import SessionLocal, Session
from tables import User, Post

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/get-posts/")
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return [
        {"id": post.id, "title": post.title, "user_id": post.owner.name} for post in posts
    ]

@app.get("/get-post/{id}")
def get_post(id:int,db:Session=Depends(get_db)):
    post=db.query(Post).filter(Post.id==id).first()
    return{
        "id":post.id,
        "name":post.title,
        "user":post.owner.name
    }

@app.post("/user/")
def create_user(name: str, db: Session = Depends(get_db)):
    user = User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@app.post("/post/")
def create_post(title: str, user_id: int, db: Session = Depends(get_db)):
    post = Post(title=title, user_id=user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
