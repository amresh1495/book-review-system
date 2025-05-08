from fastapi import FastAPI
from app.api.endpoints import books, reviews

app = FastAPI(
    title="Book Review System API",
    version="0.1.0",
    description="An API for managing books and their reviews."
)

app.include_router(books.router, prefix="/books", tags=["books"])
app.include_router(reviews.router, prefix="/reviews", tags=["reviews"])
