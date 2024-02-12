# Create Item To Purchase class
class ItemToPurchase:
    def __init__(self):
        # Initialize variables
        self.item_name = "none"
        self.item_price = float(0)
        self.item_quantity = 0

    # Print item method
    def print_item_cost(self):
        total_price = self.item_price * self.item_quantity
        print(self.item_name + ' ' + str(self.item_quantity) + ' @ ${:,.2f}'.format(self.item_price) + '= ${:,.2f}'.format(total_price))


# Main code

# Initialize list of items
list_items = []
for j in range(2):  # Loop through 2 times, can change later or modify to prompt user to end input
    # Instantiate class and add to list
    list_items.append(ItemToPurchase())
    list_items[j].item_name = str(input("Enter the item name: "))
    try:  # Ensure price is number, exit if not
        list_items[j].item_price = float(input("Enter the item price: "))
    except ValueError:
        print("Your input for price was not a number, run program again and enter valid price")
        exit()
    try:  # Ensure quantity is number, exit if not
        list_items[j].item_quantity = int(input("Enter the item quantity: "))
    except ValueError:
        print("Your input for quantity was not a number, run program again and enter valid quantity")
        exit()

# Print required output
total_cost = 0
print("Total Cost")
i = 0
while i < len(list_items):  # Loop through list of item objects, run print method, and calculate/print total cost
    list_items[i].print_item_cost()
    total_cost += list_items[i].item_price * list_items[i].item_quantity
    i += 1
print('Total: ' + '${:,.2f}'.format(total_cost))

