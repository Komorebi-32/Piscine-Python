from book import Book
from recipe import Recipe
from datetime import datetime


lasagna = Recipe("Lasagnas", 3, 64, ["eggs", "An Italian Mom", "a pinch of love"], "The best lasagnas in the world", "lunch")
bruschetta = Recipe("Bruschettas", 1, 3, ["mozza", "tomato", "gooood bread"], "Simple is Beautiful", "starter")
tiramisu = Recipe("Tiramisu", 4, 320, ["mascarpone al dente"], "Gimme Gimme Gimme Moore", "dessert")

caprese = Recipe("Caprese", 1, 10, ["mozzarella", "tomato", "basil"], "Classic Italian salad", "starter")
arancini = Recipe("Arancini", 3, 45, ["rice", "mozzarella", "breadcrumbs"], "Sicilian fried rice balls", "starter")

risotto = Recipe("Risotto alla Milanese", 4, 35, ["rice", "saffron", "parmesan"], "Creamy saffron risotto", "lunch")
osso_buco = Recipe("Osso Buco", 5, 120, ["veal shanks", "white wine", "vegetables"], "Braised veal specialty from Milan", "lunch")

panna_cotta = Recipe("Panna Cotta", 2, 20, ["cream", "sugar", "gelatin"], "Silky Italian dessert", "dessert")
cannoli = Recipe("Cannoli", 4, 60, ["ricotta", "flour", "sugar"], "Crispy Sicilian pastry", "dessert")

recipes_list = {
    "starter": [bruschetta, caprese, arancini],
    "lunch": [lasagna, risotto, osso_buco],
    "dessert": [tiramisu, panna_cotta, cannoli]
}
yummy_book = Book("Yummy Book!", datetime.now(), recipes_list)

print("-----------get_recipe_by_name() tests----------\n")
print("Should find Lasagnas:\n")
yummy_book.get_recipe_by_name("Lasagnas")
print("Should find Tiramisu:\n")
yummy_book.get_recipe_by_name("Tiramisu")
print("Should not find anything (input abc):\n")
yummy_book.get_recipe_by_name("abc")

print("\n-----------get_recipes_by_types() tests----------\n")
print("Should find all the starter meals:\n")
yummy_book.get_recipes_by_types("starter")

print("\n-----------add_recipe() tests----------\n")
print("Should add a recipe for a cafecito:\n")
cafecito = Recipe("cafecito", 1, 3, ["cafe", "leche", "azucar"], "mejor cafecito del mundo", "dessert")
yummy_book.add_recipe(cafecito)
yummy_book.get_recipe_by_name("cafecito")
