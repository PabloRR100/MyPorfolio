# prihject/api/db.py
"""
The engine is one for the whole application.

Create a new session for each group of operations with the database 
that belong together.

We should normally have one session per request in most of the cases.
In some isolated cases we would want to have new sessions inside, so, 
more than one session per request.
But we would NEVER want to share the same session among different requests.

We can work this aroung passing the session object as a dependency
"""
from sqlmodel import SQLModel, create_engine

from api.config import get_settings


SETTINGS = get_settings()
engine = create_engine(SETTINGS.DATABASE_URL)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()