import uuid
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t

from . import models, schemas


def get_job(db: Session, job_id: str):
    job = db.query(models.Job).filter(models.Job.job_id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


def get_jobs(
    db: Session, skip: int = 0, limit: int = 100
) -> t.List[schemas.JobList]:
    return db.query(models.Job).offset(skip).limit(limit).all()


def create_job(db: Session):
    job = models.Job(status="in_progress", job_id=uuid.uuid4())
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


def update_job(db: Session, job: models.Job, result: int, status: str):
    job.result = result
    job.status = status
    db.add(job)
    db.commit()
    db.refresh(job)
    return job
