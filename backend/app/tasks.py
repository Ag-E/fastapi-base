import sys
from typing import Callable
from app.core.celery_app import celery_app
from app.core.substring import SubStringService
from sqlalchemy.orm.session import Session
from app.db.session import DatabaseSession, session_manager


from app.db import crud


@celery_app.task(acks_late=True)
def example_task(word: str) -> str:
    return f"test task returns {word}"


@celery_app.task(
    name="app.tasks.calculate_substring_task",
    bind=True,
    soft_time_limit=120,
    time_limit=120,
)
def calculate_substring_task(
    self,
    word: str,
    job_id: str,
    session_factory: Callable[[], Session] = DatabaseSession,
) -> int:
    print("Word: ", word, file=sys.stderr)
    print("Job ID:", job_id, file=sys.stderr)
    result = SubStringService.find_longest_str_len(word)
    with session_manager(session_factory) as db:
        job = crud.get_job(db, job_id)
        crud.update_job(db, job, result=result, status="completed")
        return result
