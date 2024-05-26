from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, INTEGER

from app.models import Base

class User(Base):
    __tablename__ = 'user'
    
    id = Column('User.id', INTEGER, primary_key=True, nullable=False)
    username = Column('User.username', TEXT(45))
    email = Column('User.email', TEXT(45))
    password = Column('User.password', TEXT(45))
    firstname = Column('User.firstname', TEXT(45))
    lastname = Column('User.lastname', TEXT(45))
    usercol = Column('Usercol', TEXT(45))
    character = Column('Character_Character.id', INTEGER, ForeignKey(f'character.Characterid'), nullable=False)