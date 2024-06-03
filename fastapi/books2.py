from typing import Optional

from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length= 2, max_length=100)
    description: str = Field(min_length=2)
    rating: int = Field(gt=-1, lt=6)
    published_date: int = Field(gt=1800, lt=2024)

    class Config:
        json_schema_extra = {
            'example': {
                'title': 'A new book',
                'author': 'An author',
                'description': 'A new description of a book',
                'rating': 5,
                'published_date': 2012
            }
        }


BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5, 2012),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5, 2014),
    Book(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5, 2020),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2, 2010),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3, 2012),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1, 2020)
]


@app.get('/books', status_code=status.HTTP_200_OK)
async def read_al_books():
    return BOOKS


@app.get('/books/{book_id}', status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Libro no encontrado")


@app.get('/books/', status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


@app.get('/books/by_date/', status_code=status.HTTP_200_OK)
async def read_book_by_date(book_date: int = Query(gt=1900, lt=2031)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == book_date:
            books_to_return.append(book)
    return books_to_return


@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))


@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i].id = book
            return {"message": "Libro actualizado exitosamente"}
    raise HTTPException(status_code=404, detail="Libro no encontrado")


@app.delete("/books/delete_book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            return {"message": "Libro eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Libro no encontrado")


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) < 1 else BOOKS[-1].id + 1
    return book

