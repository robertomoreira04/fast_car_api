from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_car_api.models import Car
from fast_car_api.database import get_session
from fast_car_api.schemas import CarPublic, CarSchema, CarList

router = APIRouter(
    prefix='/api/v1/cars',
    tags=['cars'],
)


@router.post(
        path='/', 
        response_model=CarPublic, 
        status_code=status.HTTP_201_CREATED
)
def create_car(car: CarSchema,session: Session = Depends(get_session)):
    car = Car(**car.model_dump())
    session.add(car)
    session.commit()
    session.refresh(car)
    return car


@router.get(
    path='/',
    response_model=CarList,
    status_code=status.HTTP_200_OK,
)
def list_cars(
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = 100,
):
    query = session.scalars(select(Car).offset(offset). limit(limit))
    cars = query.all()
    return {'cars': cars}


@router.get(
    path='/{car_id}',
    response_model=CarPublic,
    status_code=status.HTTP_200_OK,
)
def get_car(
    car_id: int,
    session: Session = Depends(get_session),
):
    car = session.get(Car, car_id)
    if not car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='CAr not found',
        )
    return car