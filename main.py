from fastapi import FastAPI

app = FastAPI()

var1 = "Hola Mundo"

def foo():
    x = 1
    y = 2
    z = 3
    a = 4
    b = 5
    c = 6
    d = 7
    e = 8
    f = 9
    return x + y + z + a + b + c + d + e + f

def bar():
    x = 1
    y = 2
    z = 3
    a = 4
    b = 5
    c = 6
    d = 7
    e = 8
    f = 9
    return x + y + z + a + b + c + d + e + f

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