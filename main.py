from fastapi import FastAPI

app = FastAPI()

var1 = "Hola Mundo"

x = 25

if x < 2:
    var2 = "Hola"
elif x < 5:
    var2 = "Mundo"
elif x < 10:
    var2 = "Hola Mundo"
elif x < 20:
    var2 = "Hola Mundo!"
else:
    var2 = "Hola Mundo!!"

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