import tkinter

class PizzaStock:  
    def __init__(self):
        self.stock = {
            1: ["Pepperoni_Pizza", 120.34],  
            2: ["Cheese_Pizza", 320.34]
        }
        self.user_cart = []  # List for storing selected items

    # Display items in stock
    def output_front_store(self):
        for item_id, (name, price) in self.stock.items():
            print(f"Item ID: {item_id}, Name: {name}, Price: ${price:.2f}")

    # Store selected item in user cart
    def getdata_user(self, item_id):
        if item_id in self.stock:
            self.user_cart.append(self.stock[item_id])
            print(f"Item added to user cart: {self.stock[item_id][0]} - ${self.stock[item_id][1]:.2f}")
        else:
            print("Invalid selection. Please choose a valid item.")
        print(f"Current user items: {self.user_cart}")

    # Show all items in the user cart
    def show_cart(self):
        if self.user_cart:
            print("Items in user cart:")
            for item in self.user_cart:
                print(f"{item[0]} - ${item[1]:.2f}")
        else:
            print("No items in cart.")

class Bucket:
    def __init__(self, user_cart):
        self.user_cart = user_cart

    def remove_last_item(self):
        if self.user_cart:
            removed_item = self.user_cart.pop()
            print(f"Removed item: {removed_item[0]} - ${removed_item[1]:.2f}")
        else:
            print("No items to remove.")

# Instantiate PizzaStock
front = PizzaStock()
front.output_front_store()

while True:
    try:
        user = int(input("Choose an item by ID (0 to exit): "))
        if user == 0:
            break
        else:
            front.getdata_user(user)
    except ValueError:
        print("Error: Invalid input, please enter a valid item ID.")

# Show final cart
front.show_cart()

# Instantiate Bucket for removal actions
bucket = Bucket(front.user_cart)

while True:
    try:
        delete = input("Would you like to remove the last item? (yes to remove / no to exit): ").lower()
        if delete == "no":
            break
        elif delete == "yes":
            bucket.remove_last_item()
        else:
            print("Invalid choice. Please type 'yes' or 'no'.")
    except KeyboardInterrupt:
        print("Exiting removal process.")
        break
