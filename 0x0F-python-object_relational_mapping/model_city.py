#!/usr/bin/python3
""" cities model """
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """ creating table named 'cities' has 3 rows """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
