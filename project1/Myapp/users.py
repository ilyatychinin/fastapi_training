from fastapi import APIRouter, HTTPException, Body, Depends
from typing import Optional, Annotated

from sqlalchemy.orm import Session
from Myapp.models import User, Post
from database import engine, get_db, session_local, Base
from Myapp.schemas import UserCreate, User as DbUser

router = APIRouter()

db: Session = session_local()

@router.post("/users", response_model=DbUser)
async def create_user(user: UserCreate, db: Session = Depends(get_db)) -> DbUser:
    db_user = User(name=user.name, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

@router.get("/users", response_model=list[DbUser])
async def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()
# @router.get("/users")
# async def users() -> list[User]:
#     return [User(**user) for user in users_list]

# @router.get("/searchU")
# async def searchU(user_id: Optional[int] = None) -> dict[str, Optional[User]]:
#     if user_id:
#         for user in users_list:
#             if user['id'] == user_id:
#                 return { "data" : User(**user) }
#         raise HTTPException(status_code=404, detail='Ошибка 404')
#     else:
#         return {"data": None}
    

# @router.post("/users/add")
# async def add_user(user: Annotated[
#     UserCreate,
#     Body(..., example={
#         "name": "user_name",
#         "age": 1
#     })
# ]) -> User:
#     new_user_id = len(users_list) + 1
    
#     new_user = {'id': new_user_id, 'name': user.name, 'age' : user.age}
#     users_list.append(new_user)
#     return User(**new_user)
