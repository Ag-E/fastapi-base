import sys
import typing as t
from hashlib import new
from turtle import clear

from app import tasks
from app.core.celery_app import celery_app
from app.db.crud import create_job, get_job, get_jobs
from app.db.schemas import Job, JobCalculateRequest
from app.db.session import get_db
from fastapi import APIRouter, Depends, Request, Response, encoders

jobs_router = r = APIRouter()


@r.get(
    "/results",
    response_model=t.List[Job],
    response_model_exclude_none=True,
)
async def jobs_list(
    response: Response,
    db=Depends(get_db),
):
    """
    Get all jobs
    """
    jobs = get_jobs(db)
    # This is necessary for react-admin to work
    response.headers["Content-Range"] = f"0-9/{len(jobs)}"
    return jobs


@r.get(
    "/results/{job_id}",
    response_model=Job,
    response_model_exclude_none=True,
)
async def get_job_details(
    request: Request,
    job_id: str,
    db=Depends(get_db),
):
    """
    Get any job details
    """
    job = get_job(db, job_id)
    return job


@r.post(
    "/calculate",
    response_model=Job,
    response_model_exclude_none=True,
    status_code=201,
)
async def calculate(
    request: Request,
    job_request: JobCalculateRequest,
    db=Depends(get_db),
):
    """
    Create a new job
    """
    new_job = create_job(db)
    print(job_request.word, file=sys.stderr)
    print(new_job.job_id, file=sys.stderr)
    celery_app.send_task(
        "app.tasks.calculate_substring_task",
        args=[job_request.word, new_job.job_id],
    )
    return new_job
