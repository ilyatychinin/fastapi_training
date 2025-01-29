from fastapi import APIRouter, HTTPException
from typing import Optional
from Myapp.models import User, users_list

router = APIRouter()

@router.get("/users")
async def users() -> list[User]:
    return [User(**user) for user in users_list]

@router.get("/searchU")
async def searchU(user_id: Optional[int] = None) -> dict[str, Optional[User]]:
    if user_id:
        for user in users_list:
            if user['id'] == user_id:
                return { "data" : User(**user) }
        raise HTTPException(status_code=404, detail='Ошибка 404')
    else:
        return {"data": None}