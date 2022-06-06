#!/usr/bin/env python3
from app.db.session import SessionLocal


def init() -> None:
    db = SessionLocal()


if __name__ == "__main__":
    print("Creating superuser admin@performer.com")
    init()
    print("Superuser created")
