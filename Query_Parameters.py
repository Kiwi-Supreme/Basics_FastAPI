from fastapi import FastAPI
from typing import Optional

app = FastAPI()

#Written like this : http://127.0.0.1:8000/blog?limit=15&published=true
@app.get('/blog')
def index(limit = 10, published:bool = True, sort: Optional[str] = None): #defining their data type and default value
    # only get 10 published blogs
    if published:
        return {'data' : f'{limit} published blogs from the db'}
    else:
        return {'data' : f'{limit} blogs from the db'}
    
@app.get('/blog/{id}/comments')
def commenting(id, limit=10):
    #fetch comments of blog with id = id
    return {'data' : {'1','2'}}
