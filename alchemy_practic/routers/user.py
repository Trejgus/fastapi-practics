from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_database

from services import user as service
from schemas.user import UserSchemas

router = APIRouter(
    tags = ['auth']
)

@router.get('/user')
def get_user(username: str, db: Session = Depends(get_database)):
    user = service.get_user(db, username)
    return user


@router.post('/user/create')
def create_user(userdata: UserSchemas, db: Session = Depends(get_database)):
    user = service.create_user(db, userdata)
    return user


@router.put('/user')
def put_user(username: str, userdata: UserSchemas, db: Session = Depends(get_database)):
    user = service.update_user_data(db, username, userdata)
    return user


@router.delete('/user')
def delete_user(username: str, db: Session = Depends(get_database)):
    status = service.remove_user(db, username)
    if status:
        return {'status': 201}
    else:
        return {'status': 400}