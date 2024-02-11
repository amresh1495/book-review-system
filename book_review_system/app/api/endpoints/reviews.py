from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.api.database.database import get_db
from app.api.database import crud
from app.models.review import ReviewCreate, ReviewOut

router = APIRouter()

# Dependency to get the database session


def get_db_session():
    db = get_db()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ReviewOut)
async def create_review(review: ReviewCreate, db: Session = Depends(get_db_session)):
    return crud.create_review(db, review)
