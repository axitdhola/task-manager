from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello async World"}

@app.post("/id")
async def printId(id: int):
    return {"id": 'Hello ' + str(id) + ' World'}