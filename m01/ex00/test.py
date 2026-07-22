from book import Book
from recipe import Recipe
from datetime import datetime


lasagna = Recipe("Lasagnas", 3, 64, ["eggs", "An Italian Mom", "a pinch of love"], "The best lasagnas in the world", "lunch")
bruschetta = Recipe("Bruschettas", 1, 3, ["mozza", "tomato", "gooood bread"], "Simple is Beautiful", "starter")
tiramisu = Recipe("Tiramisu", 4, 320, ["mascarpone al dente"], "Gimme Gimme Gimme Moore", "dessert")
recipes_list = {
    "starter": bruschetta,
    "lunch": lasagna,
    "dessert": tiramisu
}
yummy_book = Book("Yummy Book!", datetime.now(), recipes_list)

yummy_book.get_recipe_by_name("Lasagnas")
yummy_book.get_recipe_by_name("Tiramisu")
yummy_book.get_recipe_by_name("abc")
