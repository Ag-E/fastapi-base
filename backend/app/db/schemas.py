import string
from pydantic import BaseModel
import typing as t


class JobBase(BaseModel):
    job_id: t.Optional[str] = None
    result: t.Optional[int] = 0
    status: t.Optional[str] = None


class Job(JobBase):
    id: int

    class Config:
        orm_mode = True


class JobList(JobBase):
    pass


class JobCreate(JobBase):
    job_id: str


class JobCalculateResponse(JobBase):
    job_id: str


class JobCalculateRequest(BaseModel):
    word: str
