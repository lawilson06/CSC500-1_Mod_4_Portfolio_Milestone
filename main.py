"""
CSC500-1 Module 4 Portfolio Milestone
Lawrence Wilson
July 6, 2025
"""

from ItemToPurchase import ItemToPurchase
from ShoppingCart import ShoppingCart

user_items = []

# Function to obtain user inputs for two items as outlined in assignment (name, quantity, and price) try-except
def user_inputs():
    print("Enter Two Items ✏✏")
    print("----------------------")
    for i in range(2):
        while True:
            try:
                temp_name = input("Enter the item name: ")
                temp_quantity = int(input("Enter the item quantity: "))
                temp_price = float(input("Enter the item price: "))
                temp_item_dict = {
                    'user_item_name': temp_name,
                    'user_item_quantity': temp_quantity,
                    'user_item_price': temp_price,
                }
                user_items.append(temp_item_dict)
                break
            except ValueError as e:
                print(e, "Must enter a valid value.")

user_inputs()
shopping_cart = ShoppingCart()

# Creating first item object and adding to shopping cart
item1 = ItemToPurchase()
item1.set_item_name(user_items[0]['user_item_name'])
item1.set_item_quantity(user_items[0]['user_item_quantity'])
item1.set_item_price(user_items[0]['user_item_price'])
shopping_cart.set_shopping_item(item1)

#Creating second item object and adding to shopping cart
item2 = ItemToPurchase()
item2.set_item_name(user_items[1]['user_item_name'])
item2.set_item_quantity(user_items[1]['user_item_quantity'])
item2.set_item_price(user_items[1]['user_item_price'])
shopping_cart.set_shopping_item(item2)

shopping_list = shopping_cart.get_shopping_list()

# Printing total cost for each item
for item in shopping_list:
    item.print_item_cost()
    print("-----------------------------")

#Printing total cost using overloaded addition operator
print(f"Total Cost: ${(shopping_list[0] + shopping_list[1]):.2f}")