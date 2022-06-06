from xml.etree.ElementInclude import include
from celery import Celery

celery_app = Celery(
    "worker",
    backend="redis://redis:6379/0",
    broker="redis://redis:6379/0",
    include=["app.tasks"],
)

celery_app.conf.task_routes = {"app.tasks.*": "main-queue"}

celery_app.autodiscover_tasks()
