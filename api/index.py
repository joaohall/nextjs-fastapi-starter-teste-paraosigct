from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/api/")
def root():
    return {"message": "API root"}

@app.get("/api/hello")
def hello():
    return {"message": "Hello from FastAPI"}

handler = Mangum(app)