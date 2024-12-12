from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()


@app.get('/')
def home():
    return {'data': "message"}

posts = [
    {'id': 1,
     'name': 'harry'},
     {'id': 2,
     'name': 'harry'},
     {'id': 3,
     'name': 'harry'}
]

@app.get('/items')
async def items() -> list[dict]:
    return posts

@app.get('/items/{id}')
async def items(id:int) -> dict:
    for i in posts:
        if i['id'] == id:
            return i
        
    raise HTTPException(status_code=404, detail='Упссс')


@app.get('/search')
async def items(post_id: Optional[int] = None) -> dict:
    if post_id:
        for i in posts: 
            if i['id'] == post_id:
                return i
        raise HTTPException(status_code=404, detail='Упссс')
    else:
        return {'data': 'wsrgwr'}
