from fastapi import Body, FastAPI

app = FastAPI()

@app.get("/post")
async def get_post():
    return{"message": "this is your post "}

@app.post("/post") 
async def create_post(payload:dict = Body(...)):
    #print(payload)
    return{"message": "created post"}

@app.patch("/post") 
async def get_post():
    return{"message": "updated post"}

@app.delete("/post") 
async def get_post():
    return{"message": "deleted post"}

