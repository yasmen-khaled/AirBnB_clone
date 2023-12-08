#!/usr/bin/python3
"""Module."""
from models.base_model import BaseModel


class Review(BaseModel):
    """class for the review info"""

    place_id = ""
    user_id = ""
    text = ""
