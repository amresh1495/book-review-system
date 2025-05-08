from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_book():
    response = client.post(
        "/books/", json={"title": "Test Book", "author": "Test Author", "publication_year": 2022})
    assert response.status_code == 201
    assert response.json()["title"] == "Test Book"


def test_create_review():
    book_data = {"title": "Test Book for Review", "author": "Test Author", "publication_year": 2023}
    response = client.post("/books/", json=book_data)
    assert response.status_code == 201 # Ensure book creation is successful
    created_book_id = response.json()["id"]

    review_data = {"text": "Great Book!", "rating": 5, "book_id": created_book_id}
    response = client.post("/reviews/", json=review_data)
    assert response.status_code == 201
    assert response.json()["text"] == "Great Book!"
    assert response.json()["book_id"] == created_book_id


def test_create_review_invalid_rating_too_low():
    book_data = {"title": "Test Book for Invalid Review Low", "author": "Test Author", "publication_year": 2023}
    response = client.post("/books/", json=book_data)
    assert response.status_code == 201
    created_book_id = response.json()["id"]

    response = client.post(
        "/reviews/", json={"text": "Rating too low", "rating": 0, "book_id": created_book_id}
    )
    assert response.status_code == 422  # Unprocessable Entity


def test_create_review_invalid_rating_too_high():
    book_data = {"title": "Test Book for Invalid Review High", "author": "Test Author", "publication_year": 2023}
    response = client.post("/books/", json=book_data)
    assert response.status_code == 201
    created_book_id = response.json()["id"]

    response = client.post(
        "/reviews/", json={"text": "Rating too high", "rating": 6, "book_id": created_book_id}
    )
    assert response.status_code == 422


def test_create_review_valid_rating_boundary_min():
    book_data = {"title": "Test Book for Review Min Rating", "author": "Test Author", "publication_year": 2023}
    response = client.post("/books/", json=book_data)
    assert response.status_code == 201
    created_book_id = response.json()["id"]

    response = client.post(
        "/reviews/", json={"text": "Valid rating min", "rating": 1, "book_id": created_book_id}
    )
    assert response.status_code == 201
    assert response.json()["rating"] == 1
    assert response.json()["book_id"] == created_book_id


def test_create_review_valid_rating_boundary_max():
    book_data = {"title": "Test Book for Review Max Rating", "author": "Test Author", "publication_year": 2023}
    response = client.post("/books/", json=book_data)
    assert response.status_code == 201
    created_book_id = response.json()["id"]

    response = client.post(
        "/reviews/", json={"text": "Valid rating max", "rating": 5, "book_id": created_book_id}
    )
    assert response.status_code == 201
    assert response.json()["rating"] == 5
    assert response.json()["book_id"] == created_book_id
