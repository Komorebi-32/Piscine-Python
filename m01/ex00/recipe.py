import sys


class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        try:
            if (
                name is None
                or cooking_lvl is None
                or cooking_time is None
                or ingredients is None
                or recipe_type is None
                or name == ""
                or ingredients[0] == ""
                or cooking_time < 0
            ):
                print("Input error: One of the required args is empty or has the wrong format")
                sys.exit(1)
            if cooking_lvl < 1 or cooking_lvl > 5:
                print("The cooking level can range from 1 to 5")
                sys.exit(1)
            if recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert":
                print("The recipe type can be \"starter\", \"lunch\" or \"dessert\"")
                sys.exit(1)
            self.name = name
            self.cooking_lvl = cooking_lvl
            self.cooking_time = cooking_time
            self.ingredients = ingredients
            self.description = description
            self.recipe_type = recipe_type
        except ValueError:
            print("Input error: One of the required args has the wrong format")
            sys.exit(1)

    def __str__(self):
        """Returns the string to print with the recipe’s info"""
        txt = ""
        txt += self.name + '\n'
        txt += "Cooking level: " + str(self.cooking_lvl) + '\n'
        txt += "Cooking time: " + str(self.cooking_time) + '\n'
        txt += "Ingredients: " + str(self.ingredients) + '\n'
        txt += "Description: " + str(self.description) + '\n'
        txt += "Recipe type: " + self.recipe_type + '\n'
        return txt
