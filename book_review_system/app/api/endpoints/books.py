from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.api.database.database import get_db
from app.api.database import crud
from app.models.book import BookCreate, BookOut

router = APIRouter()


@router.post("/", response_model=BookOut, status_code=status.HTTP_201_CREATED)
async def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)
