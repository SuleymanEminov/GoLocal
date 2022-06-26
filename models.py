from ctypes.wintypes import FLOAT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import INT

Base = declarative_base()

class Market(Base):
    __tablename__ = 'markets'
    id = Column(UUID, primary_key=True)
    name = Column(String)
    location_x = Column(FLOAT)
    location_y = Column(FLOAT)
    points = Column(INT)