from fastapi import FastAPI

app = FastAPI()

#Path paremeters
@app.get('/')
def index():
    return {'data' : {'blog list'}}

#FastAPI reads code line by line that is why, we have put '/unpublished' before '/{id}' 

@app.get('/blog/unpublished')
def unpublished():
    return {'data' : 'all unpublished blogs'}

#DEFINE THE DATA TYPE OF ID
@app.get('/blog/{id}')
def value(id:int):
    #fetch blog with id = id
    return {'data' : id}

@app.get('/blog/{id}/comments')
def commenting(id):
    #fetch comments of blog with id = id
    return {'data' : {'1','2'}}
