from sqlalchemy import Column, String, text, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, INTEGER

from app.models import Base

class Character(Base):
    __tablename__ = 'character'
    
    id = Column('Characterid', INTEGER, primary_key=True, nullable=False)
    name = Column('Charactername', TEXT(45), nullable=True)
