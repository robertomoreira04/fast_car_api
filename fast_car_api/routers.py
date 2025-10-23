from fastapi import APIRouter

router = APIRouter(
    prefix='/api/v1/cars',
    tags=['cars'],
)

@router.get('/')
def list_cars():
    return {
        'cars': [
            {'id': 1, 'modelo': 'Peugeot 206'},
            {'id': 2, 'modelo': 'Lancer 2014'},
            {'id': 3, 'modelo': 'Corolla 2025'},
        ]
    }

