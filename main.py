from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

class Post(BaseModel):
    title:str
    username:str
    published:bool = True
    rating : Optional[int] = None
 

app = FastAPI()

@app.get("/post")
async def get_post():
    return{"message": "this is your post "}

@app.post("/post") 
async def create_post(payload:Post):
    #payload:dict = Body(...)
    #print(payload)
    #return{"message": f"post title : {payload['title']} , username:{payload['username']}"}
    print("Title :" , payload.title)
    print("UserName :" , payload.username)
    print("Published Status :" , payload.published)
    print("Stars :" , payload.rating)
    return{"Title :" : payload.title,
           "UserName :" : payload.username,
           "Published Status :" : payload.published,
           "Stars :" : payload.rating }

@app.patch("/post") 
async def get_post():
    return{"message": "updated post"}

@app.delete("/post") 
async def get_post():
    return{"message": "deleted post"}

