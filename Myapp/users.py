from fastapi import APIRouter, HTTPException, Body
from typing import Optional, Annotated

router = APIRouter()

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
