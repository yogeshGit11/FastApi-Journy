from db import Base,engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


# Models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    posts = relationship("Post", back_populates="owner")

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="posts")

Base.metadata.create_all(bind=engine)
