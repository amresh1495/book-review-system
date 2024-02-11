from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.api.database.database import get_db
from app.api.database import crud
from app.models.book import BookCreate, BookOut

router = APIRouter()

# Dependency to get the database session


def get_db_session():
    db = get_db()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=BookOut)
async def create_book(book: BookCreate, db: Session = Depends(get_db_session)):
    return crud.create_book(db, book)
