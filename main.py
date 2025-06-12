from fastapi import FastAPI

app = FastAPI()

var1 = "Hola Mundo"

def foo():
    x = 1
    y = 2
    return x + y

def bar():
    x = 1
    y = 2
    return x + y

def bbb():
    x = 1
    y = 2
    return x + y

def aaa():
    x = 1
    y = 2
    return x + y

@app.get("/")
async def root():
    return {"message": var1}