#!/usr/bin/python3
"""City class definition"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))
