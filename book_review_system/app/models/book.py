from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    publication_year: int


class BookCreate(BookBase):
    pass


class BookOut(BookBase):
    id: int


class BookInDB(BookOut):
    pass
