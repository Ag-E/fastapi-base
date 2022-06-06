from urllib import response
from app.db import models
from conftest import test_job


def test_get_jobs(client):
    response = client.get("/api/v1/jobs")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": test_job.id,
            "job_id": test_job.job_id,
            "status": test_job.status,
            "result": test_job.result,
        }
    ]


def test_get_job(client):
    response = client.get(
        f"/api/v1/results/{test_job.job_id}",
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": test_job.id,
        "job_id": test_job.job_id,
        "status": test_job.status,
        "result": test_job.result,
    }


def test_calculate(client):
    response = client.post(
        "/api/v1/calculate",
        data={
            "word": "pwwkew",
        },
    )
    assert response.status_code == 201
    assert response.json() == {
        "job_id": "9c1e1cf6-7e5e-4fd9-9d09-d1ce1916f9cb",
        "status": "in_progress",
        "id": 35,
    }


def test_job_not_found(client):
    response = client.get("/api/v1/jobs/9c1e1cf6-7e5e-4fd9-9d09-d1ce1916f9ack")
    assert response.status_code == 404
