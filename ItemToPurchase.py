"""
Item class with attributes for item name, price, quantity, and the total cost which is derived from the private
calculate_cost method.
Addition operator is overloaded to allow for two ItemToPurchase objects to be added together
Basic setters and print item cost method
"""

class ItemToPurchase:
    def __init__(self):
        self.__item_name = "none"
        self.__item_price = 0
        self.__item_quantity = 0
        self.__total_cost = 0

    def __calculate_cost(self):
        self.__total_cost = self.__item_price * self.__item_quantity

    def set_item_name(self, name):
        self.__item_name = name

    def set_item_price(self, price):
        self.__item_price = price

    def set_item_quantity(self, quantity):
        self.__item_quantity = quantity

    def print_item_cost(self):
        self.__calculate_cost()
        print(f"{self.__item_name} {self.__item_quantity} @ ${self.__item_price:.2f} = ${self.__total_cost:.2f}")

    def __add__(self, other):
        self.__calculate_cost()
        other.__calculate_cost()
        return self.__total_cost + other.__total_cost
