
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


if __name__ == "__main__":
    cookbook.pop("Cake")
    s = input("Input a recipe\n")
    print_recipe_details(s)
