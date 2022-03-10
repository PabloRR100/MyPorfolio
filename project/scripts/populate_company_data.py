from unicodedata import name
from sqlmodel import Session

from api.constants import CompanyName, Exchange as Exchange_
from api.schemas import Exchange
from api.db import engine


def add_exchanges():
    with Session(engine) as session:
        for exchange in Exchange_.all_values():
            session.add(Exchange(name=exchange))
        session.commit()
    session.close()
    return

