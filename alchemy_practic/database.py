from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

DATABASE_URL = 'sqlite:///database.db'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind = engine)
Base = declarative_base()

def get_database():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()