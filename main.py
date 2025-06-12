from fastapi import FastAPI

app = FastAPI()

var1 = "Hola Mund"

@app.get("/")
async def root():
    return {"message": var1}