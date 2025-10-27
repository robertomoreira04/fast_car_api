from fastapi import APIRouter

from fast_car_api.schemas import CarSchema

router = APIRouter(
    prefix='/api/v1/cars',
    tags=['cars'],
)


@router.post('/')
def create_car(car: CarSchema):
    return car
