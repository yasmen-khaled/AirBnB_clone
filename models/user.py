#!/usr/bin/python3
""" ___user class___ """
from models.base_model import BaseModel


class User(BaseModel):
    """___add user info___ """
  
    email = ""
    password = ""
    first_name = ""
    last_name = ""
