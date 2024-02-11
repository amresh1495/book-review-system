from sqlalchemy.orm import Session
from app.models.book import BookCreate, BookInDB
from app.models.review import ReviewCreate, ReviewInDB
from app.api.database.models import Book, Review


def create_book(db: Session, book: BookCreate) -> BookInDB:
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def create_review(db: Session, review: ReviewCreate) -> ReviewInDB:
    db_review = Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review
