from fastapi.testclient import TestClient
import pytest

from shapemaker.app import main


@pytest.fixture
def client():
    app = main()
    yield TestClient(app)


def test_ping(client):
    response = client.get("/ping")
    assert response.status_code == 200
