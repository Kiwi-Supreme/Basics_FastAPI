from fastapi import FastAPI

app = FastAPI()

@app.post('/blog')
def getting_data(title,body):
    return {'title' : title, 'body' : body}
