"""
file: project/models/company.py

CRUD+ functionalities for entities:
    - Exchanges
    - Companies
    - Sectors
"""
from sqlmodel import select, Session

from api.models.company import Company, Exchange, Sector
from api.db import engine


# Exchanges
## 

def create_exchange(session: Session, exchange_data: Exchange):        
    new_exchange = Exchange(name=new_exchange)
    session.add(new_exchange)
    session.commit()
    session.refresh(new_exchange)
    session.close()
    return new_exchange


def list_exchanges(session: Session):
    return session.exec(select(Exchange)).all()


def bulk_create_exchanges(session: Session):
    pass


# Companies
## 

def create_company():
    pass
