#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from models.city import City
import sqlalchemy
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    if models.store == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""


def __init__(self, *args, **kwargs):
    """creates a state instance"""
    super().__init__(*args, **kwargs)


if models.store != "db":
    @property
    def cities(self):
        """getter for list of City instances related to state"""
        city_list = []
        all_cities = models.store.all(City)
        for city in all_cities.values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
