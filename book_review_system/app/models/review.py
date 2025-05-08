from pydantic import BaseModel, Field


class ReviewBase(BaseModel):
    text: str
    rating: int = Field(..., description="The rating of the review, from 1 to 5", ge=1, le=5)
    book_id: int


class ReviewCreate(ReviewBase):
    pass


class ReviewOut(ReviewBase):
    id: int
    book_id: int

    class Config:
        orm_mode = True


class ReviewInDB(ReviewOut):
    pass
