from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.expression import null
from models.base import Base

class Color(Base):
    __tablename__ = 'colors'
    id = Column(Integer, primary_key=True)
    name = Column(String,nullable=False , unique=True)
    rgb = Column(String,nullable=True)
    favorite = Column(Boolean,nullable=True)

    