from pydantic import BaseModel


class ReviewBase(BaseModel):
    text: str
    rating: int


class ReviewCreate(ReviewBase):
    pass


class ReviewOut(ReviewBase):
    id: int


class ReviewInDB(ReviewOut):
    pass
