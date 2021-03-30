#!/usr/bin/python3
"""
State class:
inherits from Base Tips
links to the MySQL table states
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name =  Column(String(128), nullable=False)
