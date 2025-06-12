from fastapi import FastAPI

app = FastAPI()

var1 = "Hola Mundo"
var1 = "Hola Mundo"
var1 = "Hola Mundo"
#aaaaaaaaa
#

###asdas
#ccc
# bbbbbbbbbb
@app.get("/")
async def root():
    return {"message": var1}