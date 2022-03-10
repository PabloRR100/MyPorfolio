from fastapi import APIRouter, Response, status
from typing import List

from api.error_handlers import ErrorMessage
from api.models.company import Exchange
from api.services import company as company_services


router = APIRouter()


@router.post(
    "/Exchange",
    response_model=Exchange,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": ErrorMessage},
        status.HTTP_409_CONFLICT: {"model": ErrorMessage},
    },
)
def create_exchange(exchange_data: Exchange):
    new_exchange = company_services.create_exchange(
        exchange_data=exchange_data
    )
    return Exchange(**new_exchange.dict())


@router.get(
    "/Exchange",
    response_model=List[Exchange],
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": ErrorMessage},
    },
)
def list_exchanges():
    new_exchange = company_services.list_exchanges()
    return Exchange(**new_exchange.dict())
