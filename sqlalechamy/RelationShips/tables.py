from db import Base, engine
from sqlalchemy.orm import relationship,Session
from sqlalchemy import Column, Integer, String, ForeignKey


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(length=20), nullable=False)
    age = Column(Integer, nullable=False)
    posts = relationship("Post", back_populates="writer")


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String(length=50), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id))
    writer = relationship("User", back_populates="posts")


Base.metadata.create_all(engine)
