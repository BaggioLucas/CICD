from fastapi import FastAPI

app = FastAPI()

var1 = "Hola Mundo"

@app.get("/")
async def root():
    return {"message": var1}