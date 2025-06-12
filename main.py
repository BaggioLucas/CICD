from fastapi import FastAPI

app = FastAPI()

var1 = "Hola Mundo"

a = 'mensaje de prueba'

x = 5

b = 1542

@app.get("/")
async def root():
    return {"message": var1}