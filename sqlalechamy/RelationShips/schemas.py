from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    # id: int
    name: str = Field(title="User name")
    age: int = Field(title="User age", default=18, gt=18)


class PostSchema(BaseModel):
    # id: int
    title: str = Field(title="Post title", max_length=50)
    user_id: int = Field(title="User ID")
