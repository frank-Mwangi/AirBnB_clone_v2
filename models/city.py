#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
import models
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel):
    """ The city class, contains state ID and name """
    if models.store == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""


def __init__(self, *args, **kwargs):
    """initializes city"""
    super().__init__(*args, **kwargs)
