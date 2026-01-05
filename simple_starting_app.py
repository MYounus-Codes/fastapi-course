from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_message():
    return {"message" : "Hello, World!"}

@app.get("/greet/{name}")
async def greet_user(name : str) -> dict:
    return {"greeting" : f"Hello, {name}!"}

if __name__ == "__main__":

    import uvicorn
    uvicorn.run(app, host="localhost", port=8001)