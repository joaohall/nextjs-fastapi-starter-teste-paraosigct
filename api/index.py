from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/api/test")
async def root():
    return json("teste")