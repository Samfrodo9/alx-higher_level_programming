#!/usr/bin/python3

"""
	Creating a state Model
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class State(Base):
	"""A state class"""
	__table__ = states

	id =  Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
	name = Column(String(128), nullable=False)
