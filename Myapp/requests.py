import aiohttp

async def getdata(url: str):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200: 
                    try:
                        json_response = await response.json() 
                        return json_response
                    except ValueError:
                        print("Ошибка: ответ не является корректным JSON.")
                else:
                    print(f"Ошибка при получении данных. Статус: {response.status}")
        except aiohttp.ClientError as e:
            print(f"Ошибка при выполнении запроса: {str(e)}")
    return None  # Вернем None, если произошла ошибка
