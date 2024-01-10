#!/usr/bin/python3
"""Defines  City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city.

    Attributes:
        state_id (str): The state id.
        name (str): Name of the city.
    """

    state_id = ""
    name = ""
