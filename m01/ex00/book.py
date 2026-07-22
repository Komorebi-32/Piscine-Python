import sys
from datetime import datetime


class Book:
    def __init__(self, name, creation_date, recipes_list):
        if not isinstance(name, str) or name == "":  # isinstance() rejects also None variables
            print("Input Error: name must be a non-empty string")
            sys.exit(1)
        if not isinstance(creation_date, datetime):
            print("Input Error: wrong format for the creation date")
            sys.exit(1)
        if (
            not isinstance(recipes_list, dict)
            or len(recipes_list) != 3
            or "starter" not in recipes_list
            or "lunch" not in recipes_list
            or "dessert" not in recipes_list
        ):
            print("Input Error: the recipes list must be a dictionary with starter, lunch and dessert keys")
            sys.exit(1)
        self.name = name
        self.last_update = creation_date
        self.creation_date = creation_date
        self.recipes_list = recipes_list
