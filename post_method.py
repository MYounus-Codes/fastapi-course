from fastapi import FastAPI
from pydantic import BaseModel

class CreateBook(BaseModel):
    title: str
    author: str

app = FastAPI()

@app.post("/create_book/")
async def create_book(book: CreateBook) -> dict:
    return {"message": f"Book '{book.title}' by {book.author} created successfully!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8003)
