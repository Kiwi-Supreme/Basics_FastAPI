from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {'data' : {'name':'Shivani'}}
    #return 'Hello World'

@app.get('/about')
def about():
    return {'data' : {'about page'}}
