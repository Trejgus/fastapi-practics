from sqlalchemy import String, Integer, Column
from database import Base

class User(Base):
    __tablename__ = 'Users' # название таблицы
    
    id = Column(Integer(), primary_key = True)
    name = Column(String(), nullable = False)