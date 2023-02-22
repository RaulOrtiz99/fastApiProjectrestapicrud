from fastapi import FastAPI
from pydantic import BaseModel
from typing import Text,Optional
from datetime import datetime
app = FastAPI()

posts = []

#este es el esquema de la base de datos
class Post(BaseModel):
    id : Optional[str]
    author:str
    content:Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool=False

#ASI SE MANEJAN LAS RUTAS EN FASTAPI

#estos son los metodos
@app.get('/')
def read_root():
    return {"Welcome":"Welcome to my API"}

@app.get('/posts')
def get_posts():
    return posts

@app.post('/posts')
def save_post(post):
    print(post)
    return "received"