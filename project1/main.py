from fastapi import FastAPI
from Myapp.data import router as data_router
from Myapp.users import router as users_router

app = FastAPI()

# Подключаем маршруты из других файлов
app.include_router(data_router)
app.include_router(users_router)

@app.get("/")
async def home_page() -> str:
    return "Это корневой адрес, тут ничего нет"