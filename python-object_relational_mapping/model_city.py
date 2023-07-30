#!/usr/bin/python3

"""City class definition"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """City class"""
    __tablename__ = 'cities'
    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement="auto"
    )
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )

    def __init__(self, name, state_id):
        """Instantiation of City class instance"""
        self.name = name
        self.state_id = state_id
