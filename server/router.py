from fastapi import APIRouter

router = APIRouter()

@router.get('/name')
async def get_name():
    return {'namme': 'Bolaji'}
