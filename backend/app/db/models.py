import datetime
from operator import index
from sqlalchemy import Column, Integer, String, DateTime

from .session import Base


class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(String, nullable=True, index=True)
    status = Column(
        String, nullable=False, default="in_progress"
    )  # in_progress, completed, error
    result = Column(Integer, nullable=True)
    retry_count = Column(Integer, nullable=True, default=0)
    created_at = Column(DateTime, default=datetime.datetime.now())
