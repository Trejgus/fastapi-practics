from schemas.user import UserSchemas
from models.user import User
from sqlalchemy.orm import Session

def create_user(db: Session, userdata: UserSchemas):
    user = User(name = userdata.name)
    
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    
    except Exception as ex:
        print(ex)
        
    return user


def get_user(db: Session, username: str):
    return db.query(User).filter_by(name = username).first()


def update_user_data(db: Session, username: str,userdata: UserSchemas):
    user = get_user(db, username)
    user.name = userdata.name
    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user


def remove_user(db: Session, username: str):
    user = db.query(User).filter_by(name = username).delete()
    db.commit()
    return user

    
        