from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_book():
    response = client.post(
        "/books/", json={"title": "Test Book", "author": "Test Author", "publication_year": 2022})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Book"


def test_create_review():
    response = client.post(
        "/reviews/", json={"text": "Great Book!", "rating": 5})
    assert response.status_code == 200
    assert response.json()["text"] == "Great Book!"
