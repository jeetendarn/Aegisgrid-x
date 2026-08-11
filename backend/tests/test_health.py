from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "aegisgrid-x",
    }


def test_system_info():
    response = client.get("/api/v1/system/info")

    assert response.status_code == 200
    assert response.json()["application"] == "AegisGrid X"


def test_system_status():
    response = client.get("/api/v1/system/status")

    assert response.status_code == 200
    assert response.json()["status"] == "operational"
