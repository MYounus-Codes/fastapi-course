from fastapi import FastAPI

app = FastAPI()

## Using Query Parameters + Path Parameters

@app.get("/greet/{name}") 
async def greet_user(name: str, age: int) -> dict:
    return {"greeting" : f"Hello, {name}! You are {age} years old."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8002)
