from pydantic import BaseModel, Field
from typing import Optional,Annotated

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String)
    author_id = Column(Integer, ForeignKey("users.id"))
    
    author = relationship("User") # +1 поле где вся инфа про пользователя

# class User(BaseModel):
#     id: int
#     name: str
#     age: int

# users_list = [
#     {'id': 1, 'name': 'david', 'age': 43},
#     {'id': 2, 'name': 'rayan', 'age': 35},
#     {'id': 3, 'name': 'jojo', 'age': 150}
# ]

# class Post(BaseModel):
#     id: int
#     title: str
#     body: str
#     author: User

# posts = [
#     {'id': 1, 'title': "news 1", 'body': 'Text 1', 'author': users_list[0]},
#     {'id': 2, 'title': "news 2", 'body': 'Text 2', 'author': users_list[1]},
#     {'id': 3, 'title': "news 3", 'body': 'Text 3', 'author': users_list[2]}
# ]

# class PostCreate(BaseModel):
#     title: str
#     body: str
#     author_id: int


# class UserCreate(BaseModel):
#     name: Annotated[
#         str, Field(...,title='User name', min_length=2, max_length=52)
#     ]
#     age: Annotated[
#         int, Field(...,title='User age', ge=1,le=120)
#     ]

