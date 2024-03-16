#!/usr/bin/python3
"""
contains the class definition of a City
"""
from sqlalchemy import Column, ForeignKey, Integer, String

from model_state import Base


class City(Base):
    """
    Inherits from base
    has attributes, Id, state_id and name
    """
    __tablename__ = "cities"
    id = Column(Integer,
                unique=True,
                primary_key=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
