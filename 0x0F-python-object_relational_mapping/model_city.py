#!/usr/bin/python3
"""
Module defining the State class and Base instance for SQLAlchemy.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """
    State class:
    - Inherits from Base
    - Links to MySQL table states
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'),nullable=False)
    state = relationship("State")