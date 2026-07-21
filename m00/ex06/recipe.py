
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


def print_menu():
    print("List of available options:")
    print("   1: Add a recipe")
    print("   2: Delete a recipe")
    print("   3: Print a recipe")
    print("   4: Print the cookbook")
    print("   5: Quit\n")


if __name__ == "__main__":
    print("Welcome to the Python Cookbook !")
    print_menu()
    choice = 0
    while choice != 5:
        try:
            choice = int(input("Please select an option:\n"))
        except ValueError:
            print("Sorry, this option does not exist.")
            print_menu()
            continue
        match choice:
            case 1:
                add_recipe()
            case 2:
                print("\nAvailable recipes in the cookbook:")
                print_recipe_names()
                s = input("\nEnter a recipe to delete:\n")
                delete_recipe(s)
            case 3:
                print("\nAvailable recipes in the cookbook:")
                print_recipe_names()
                s = input("\nEnter a recipe to print:\n")
                print_recipe_details(s)
            case 4:
                for x in cookbook.items():
                    print(x)
            case 5:
                print("Cookbook closed. Goodbye !")
            case _:
                print("Sorry, this option does not exist.")
                print_menu()
