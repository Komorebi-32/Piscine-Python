import sys
from recipe import Recipe
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

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for recipe_type in self.recipes_list.values():
            for i in recipe_type:
                if i.name == name:
                    print(i)
                    return i
        print("Recipe does not exist")
        return None

    def get_recipes_by_types(self, recipe_type):
        """Gets all recipes names for a given recipe_type """
        if recipe_type not in self.recipes_list:
            print("Invalid recipe type")
            return []

        recipes = self.recipes_list[recipe_type]
        if not recipes:
            print("No recipe of this type exists in the cookbook")
            return []

        for recipe in recipes:
            print(recipe.name)   # or print(recipe) if you want full details
        return recipes

    def add_recipe(self, recipe):
        """Adds a recipe to the book and updates last_update"""

        if not isinstance(recipe, Recipe):
            print("Input Error: recipe must be a Recipe instance")
            sys.exit(1)
        self.recipes_list[recipe.recipe_type].append(recipe)
