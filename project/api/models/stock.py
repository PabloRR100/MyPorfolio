from inspect import trace
from lib2to3.pgen2.token import OP
from sqlmodel import Field, SQLModel, Enum
from typing import Optional


class Stock(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str  
    ticker: str
    ISIN: Optional[str]
    Exchange: Optional[str]

