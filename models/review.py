#!/usr/bin/python3
"""Defines the Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.

    Attributes:
        place_id (str): The place ID
        user_id (str): The User ID
        text (str): The text of the review
    """

    place_id = ""
    user_id = ""
    text = ""
