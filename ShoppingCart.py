# Basic preliminary framework for shopping cart class with shopping list and basic setter and getter methods

class ShoppingCart:
    def __init__(self):
        self.__shopping_list = []

    def set_shopping_item(self, item):
        self.__shopping_list.append(item)

    def get_shopping_list(self):
        return self.__shopping_list