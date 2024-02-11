from fastapi import FastAPI
from app.api.endpoints import books, reviews

app = FastAPI()

app.include_router(books.router, prefix="/books", tags=["books"])
app.include_router(reviews.router, prefix="/reviews", tags=["reviews"])
