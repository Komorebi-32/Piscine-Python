
cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}


def print_recipe_names():
    for x in cookbook.items():
        print(x[0])


def print_recipe_details(name):
    try:
        for x in cookbook[name]:
            print(cookbook[name][x])
    except KeyError:
        print("The recipe is not (yet?) in the cookbook")


def delete_recipe(name):
    try:
        cookbook.pop(name)
    except KeyError:
        print("The recipe is not (yet?) in the cookbook")


def add_recipe():
    try:
        name = input("Enter a name:\n")
        ingredients = []
        print("Enter ingredients:")
        while True:
            ingredient = input()
            if ingredient == "":
                break
            ingredients.append(ingredient)

        meal = input("Enter a meal type:\n")
        prep_time = int(input("Enter a prep time:\n"))
        cookbook[name] = {
            "ingredients": ingredients,
            "meal": meal,
            "prep_time": prep_time,
        }
    except ValueError:
        print("Prep time must be an integer")


if __name__ == "__main__":
    cookbook.pop("Cake")
    add_recipe()
    s = input("Choose a recipe to show details\n")
    print_recipe_details(s)
