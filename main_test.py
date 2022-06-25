from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_correct_item():
    response = client.get("/getweather/tehran")
    assert response.status_code == 200
    
def test_wrong_item():
    response = client.get("/getweather/fake")
    assert response.status_code == 404
    assert response.json() == {"Error": "The city not exist at all"}
