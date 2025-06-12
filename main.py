from fastapi import FastAPI

app = FastAPI()

var1 = "Se rompe el test"

@app.get("/")
async def root():
    return {"message": var1}