from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API root"}

@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI"}

# IMPORTANTE: A Vercel precisa deste handler
def handler(event, context):
    # Importa o Mangum apenas quando necessário
    from mangum import Mangum
    asgi_handler = Mangum(app)
    return asgi_handler(event, context)