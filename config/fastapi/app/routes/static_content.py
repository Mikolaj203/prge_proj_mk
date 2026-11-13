from fastapi import APIRouter


router_get_users = APIRouter()

@router_get_users.get("/users")
async def get_users():
    return [
        {'id': 1, 'name': 'bartek'},
        {'id': 2, 'name': 'emil'},
        {'id': 3, 'name': 'mikołaj'},
        {'id': 4, 'name': 'natalia'}
    ]