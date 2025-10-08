from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # Acessa via /api/index
def root():
    return {"message": "API root"}

@app.get("/hello")  # Acessa via /api/index/hello
def hello():
    return {"message": "Hello from FastAPI"}