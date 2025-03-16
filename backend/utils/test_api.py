from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_predict():
    response = client.post("/predict", json={"text": "I'm so happy today!"})
    assert response.status_code == 200
    data = response.json()
    assert "emotions" in data
    assert isinstance(data["emotions"], list)
