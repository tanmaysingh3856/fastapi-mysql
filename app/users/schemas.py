from pydantic import BaseModel, Field
from datetime import datetime


class BaseUser(BaseModel):
    first_name: str = Field(description="first name", examples=["Bob"])
    last_name: str = Field(description="last name", examples=["Ross"])
    email: str = Field(description="email", examples=["happy_accidents@gmail.com"])


class UserCreate(BaseUser):
    created: datetime = Field(description="created")


class User(BaseUser):
    id: int = Field(description="user id", examples=[1])
    created: datetime = Field(description="created")


# class UserList(list[BaseUser]):
#     pass
