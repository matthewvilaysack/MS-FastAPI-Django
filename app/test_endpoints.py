from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app) 

# Testing API Request
def test_get_home():
    response = client.get("/") #request.get("/")
    # assert response.text != // testing the actual text from the api call.
    assert response.status_code == 200
    assert  "text/html" in response.headers['content-type']

    # Testing API Request
def test_post_home():
    response = client.post("/") #request.get("/")
    assert response.status_code == 200
    assert  "application/json" in response.headers['content-type']
    # assert response.json()