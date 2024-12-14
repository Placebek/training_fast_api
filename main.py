from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field, EmailStr
from typing import Dict, List, Any, Union, Annotated

app = FastAPI()


class NameAge(BaseModel):
    name_product: str

dict_product = {
    'apple': 40,
    'orange': 50,
    'cucumber': 100,
    'pineapple': 200,
    'lemon': 20,
    'carrot': 50,

}


class User(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    age: int = Field(..., ge=0, le=100)
    email: str = EmailStr


@app.post("/tags/")
async def tags(item: List[str]) -> List[str]:
    return sorted(item)

@app.post("/tags/filter/")
async def tags(min_price: int, max_price: int) -> Dict[str, int]:
    filtered_dict = {key: value for key, value in dict_product.items() if value > min_price and value < max_price}
    return filtered_dict


@app.post("/user/registration/")
async def register(item:User) -> Dict[str, Union[str, int]]:
    return {
        'name': item.name,
        'age': item.age,
        'email': item.email,
    }

@app.post("/items/")
async def name_age(item: NameAge) -> Dict[str, str]:    
    return {"message": 
            f"{item.name_product}: {dict_product[item.name_product]}"}

@app.get("/items/{name}")
async def hello_age(name: str = Path(title="Имя пользователя")) -> Dict[str, str]:
    return {"message": 
            f"Hello {name}"}


@app.get("/add/")
async def plus_age(a: int, b: int) -> Dict[str, Any]:
    return {
        "message": {
            "result": a + b  # Результат суммы
        }
    }

