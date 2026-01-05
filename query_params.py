from fastapi import FastAPI
from typing import Optional


app = FastAPI()

## Using Query Parameters + Path Parameters

@app.get("/greet/{name}") 
async def greet_user(name: str, age: int) -> dict:
    return {"greeting" : f"Hello, {name}! You are {age} years old."}

## Using the Optional Type for Query Parameters
@app.get("/items/")
async def read_item(item_name : Optional[str] = "New Item", item_id : int = 0) -> dict:
    return {"item_id" : item_id, "item_name" : item_name}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8002)
