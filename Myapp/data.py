from fastapi import APIRouter, HTTPException, Path, Query, Depends
from typing import Optional,Annotated
from Myapp.requests import getdata
from fastapi.responses import JSONResponse
from typing import Union

from sqlalchemy.orm import Session
from Myapp.models import Base, User, Post
from database import engine,session_local
from Myapp.schemas import UserCreate, PostCreate, PostResponse, User as DbUser

router = APIRouter()

Base.metadata.create_all(bind=engine)

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

@router.post("/users", response_model=DbUser)
async def create_user(user: UserCreate, db: Session = Depends(get_db)) -> DbUser:
    db_user = User(name=user.name, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

@router.post("/posts", response_model=PostResponse)
async def create_post(post: PostCreate, db: Session = Depends(get_db)) -> Post:
    db_user = db.query(User).filter(User.id == post.author_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="пидарас не найден")
    db_post = Post(title=post.title,
                   body=post.body,
                   author_id=post.author_id
                   )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    return db_post

@router.get("/posts", response_model=list[PostResponse])
async def get_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()
# @router.get("/data")
# async def data_page() -> list:
#     return posts


# @router.get("/items/{user_id}", response_model=Union[Post, dict])
# async def items(user_id: Annotated[int, Path(...,title='Здесь указывается user_id', ge=1,lt=100)]) -> Union[Post, dict]:
#     # Ищем пост с указанным user_id
#     for post in posts:
#         if post['id'] == user_id:
#             return Post(**post)
#     # Если пост не найден, возвращаем None или другой объект

#     return {"data": "not found"}
        
# @router.get("/items")
# async def items() -> list[Post]:
#     return [Post(**post) for post in posts]

# @router.get("/search")
# async def search(post_id: Annotated[
#     Optional[int],
#     Query(title='search?post_id=id')
    
# ]) -> dict[str, Optional[Post]]:
#     if post_id:
#         for post in posts:
#             if post['id'] == post_id:
#                 return { "data" : Post(**post)}
#         raise HTTPException(status_code=404, detail='Ошибка 404')
#     else:
#         return {"data": None}
    
# @router.get("/check_dataU")
# async def check_data(user_id: Optional[int] = None) -> dict[str, str]:
#     url = f"http://127.0.0.1:8000/items/{user_id}"
#     json_obj = await getdata(url)

#     if json_obj:
#         if "author" in json_obj and json_obj["author"] is not None:
#             return {"has_author": "True"}
#         else:
#             return {"has_author": "False"}
#     else:
#         print("Ошибка: JSON не получен")
#         return {"error": "JSON не получен"}  # Добавляем return

# @router.post("/items/add")
# async def add_item(post: PostCreate) -> Post:
#     author = next((user for user in users_list if user['id'] == post.author_id), None)
#     if not author:
#         raise HTTPException(status_code=404, detail='User not found')
    
#     new_post_id = len(posts) + 1
#     new_post =  {'id': new_post_id, 'title': post.title, 'body': post.body, 'author' : author}
#     posts.append(new_post)

#     return Post(**new_post)
