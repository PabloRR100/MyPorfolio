from sqlmodel import Field, SQLModel
from typing import Optional

# from api.constants import CompanyName, Exchange


# Exchange
# ---

class Exchange(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) 
    name: str  = Field(index=True) # work with Enum
    country: Optional[str]


class Company(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) 
    name: str = Field(index=True) # work with Enum


class Sector(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) 
    name: str = Field(index=True)  # work with Enum
