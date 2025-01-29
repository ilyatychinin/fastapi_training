from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: int

users_list = [
    {'id': 1, 'name': 'david', 'age': 43},
    {'id': 2, 'name': 'rayan', 'age': 35},
    {'id': 3, 'name': 'jojo', 'age': 150}
]

class Post(BaseModel):
    id: int
    title: str
    body: str
    author: User

posts = [
    {'id': 1, 'title': "news 1", 'body': 'Text 1', 'author': users_list[0]},
    {'id': 2, 'title': "news 2", 'body': 'Text 2', 'author': users_list[1]},
    {'id': 3, 'title': "news 3", 'body': 'Text 3', 'author': users_list[2]}
]