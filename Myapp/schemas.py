from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    age: int

class User(UserBase):
    id: int
    
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    pass



class PostBase(BaseModel):
    title: str
    body: str
    author_id: int

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    author: User
    class Config:
        orm_mode = True


# class UserCreate(BaseModel):
#     name: Annotated[
#         str, Field(...,title='User name', min_length=2, max_length=52)
#     ]
#     age: Annotated[
#         int, Field(...,title='User age', ge=1,le=120)
#     ]