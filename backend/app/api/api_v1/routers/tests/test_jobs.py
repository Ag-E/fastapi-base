import json
from urllib import response
from conftest import test_job


def test_calculate(client):
    response = client.post(
        "/api/v1/calculate",
        json={
            "word": "pwwkew",
        },
    )
    assert response.status_code == 201
    assert response.json()["status"] == "in_progress"
    assert response.json()["id"] == 1


def test_not_calculate(client):
    response = client.post("/api/v1/calculate", json={"w0rd": "pwkwed"})
    assert response.status_code == 422


def test_get_jobs(client):
    response = client.post(
        "/api/v1/calculate",
        json={
            "word": "pwwkew",
        },
    )
    response = client.get("/api/v1/results")
    assert response.status_code == 200
    data = response.json()
    assert data[0]["status"] == "in_progress"
    assert data[0]["id"] == 2


def test_job_not_found(client):
    response = client.get("/api/v1/jobs/9c1e1cf6-7e5e-4fd9-9d09-d1ce1916f9ack")
    assert response.status_code == 404
