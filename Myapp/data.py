from fastapi import APIRouter, HTTPException
from typing import Optional
from Myapp.models import Post, posts
from Myapp.requests import getdata
from fastapi.responses import JSONResponse
from typing import Union

router = APIRouter()

@router.get("/data")
async def data_page() -> list:
    return posts


@router.get("/items/{user_id}", response_model=Union[Post, dict])
async def items(user_id: int) -> Union[Post, dict]:
    # Ищем пост с указанным user_id
    for post in posts:
        if post['id'] == user_id:
            return Post(**post)
    # Если пост не найден, возвращаем None или другой объект

    return {"data": "not found"}
        
@router.get("/items")
async def items() -> list[Post]:
    return [Post(**post) for post in posts]

@router.get("/search")
async def search(post_id: Optional[int] = None) -> dict[str, Optional[Post]]:
    if post_id:
        for post in posts:
            if post['id'] == post_id:
                return { "data" : Post(**post)}
        raise HTTPException(status_code=404, detail='Ошибка 404')
    else:
        return {"data": None}
    
@router.get("/check_dataU")
async def check_data(user_id: Optional[int] = None) -> dict[str, str]:
    url = f"http://127.0.0.1:8000/items/{user_id}"
    json_obj = await getdata(url)

    if json_obj:
        if "author" in json_obj and json_obj["author"] is not None:
            return {"has_author": "True"}
        else:
            return {"has_author": "False"}
    else:
        print("Ошибка: JSON не получен")
        return {"error": "JSON не получен"}  # Добавляем return


