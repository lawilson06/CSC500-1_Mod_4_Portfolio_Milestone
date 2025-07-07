from ItemToPurchase import ItemToPurchase
from ShoppingCart import ShoppingCart

user_item_names = []
user_item_quantities = []
user_item_prices = []

def user_inputs():
    temp_name = ''
    temp_quantity = 0
    temp_price = 0
    print("Enter Two Items ✏✏")
    print("----------------------")
    for i in range(2):
        while True:
            try:
                temp_name = input("Enter the item name: ")
                temp_quantity = int(input("Enter the item quantity: "))
                temp_price = float(input("Enter the item price: "))
                user_item_names.append(temp_name)
                user_item_quantities.append(temp_quantity)
                user_item_prices.append(temp_price)
                break
            except ValueError as e:
                print(e, "Must enter a valid value.")

user_inputs()
shopping_cart = ShoppingCart()

item1 = ItemToPurchase()
item1.set_item_name(user_item_names[0])
item1.set_item_quantity(user_item_quantities[0])
item1.set_item_price(user_item_prices[0])
shopping_cart.set_shopping_item(item1)

item2 = ItemToPurchase()
item2.set_item_name(user_item_names[1])
item2.set_item_quantity(user_item_quantities[1])
item2.set_item_price(user_item_prices[1])
shopping_cart.set_shopping_item(item2)

shopping_list = shopping_cart.get_shopping_list()

for item in shopping_list:
    item.print_item_cost()
    print("-----------------------------")
print(f"Total Cost: ${(shopping_list[0] + shopping_list[1]):.2f}")