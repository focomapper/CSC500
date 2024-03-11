from datetime import datetime


# Create Item To Purchase class
class ItemToPurchase:
    def __init__(self):
        # Initialize variables
        self.item_name = 'none'
        self.item_price = float(0)
        self.item_quantity = 0
        self.item_description = 'none'  # Assumed this is necessary but not in instructions

    # Print item method
    def print_item_cost(self):
        total_price = self.item_price * self.item_quantity
        print('{:^50}'.format(self.item_name + ' ' + str(self.item_quantity) + ' @ ${:,.2f}'.format(self.item_price) + ' = ${:,.2f}'.format(total_price)))


# Create Shopping Cart class
class ShoppingCart:

    cart_contents = []

    def __init__(self, name='none', date="January 1, 2020"):
        self.customer_name = name
        self.current_date = date

    def add_item(self, item):  # item to purchase
        # check if name is unique, if so prompt user to enter unique name
        item_exists = False
        for existing_item in self.cart_contents:
            if existing_item.item_name == item.item_name:
                item_exists = True
        if item_exists:
            print('{:^50}'.format('Item with name ' + item.item_name + ' already exists in cart. Please use a different name.'))
        else:
            self.cart_contents.append(item)
            print('{:^50}'.format('Item ' + item.item_name + ' added to shopping cart'))

    def remove_item(self, item_name):  # item name
        item_found = False
        for item in self.cart_contents:
            if item.item_name == item_name:
                self.cart_contents.remove(item)
                item_found = True
                print('{:^50}'.format('Item ' + item.item_name + ' removed from shopping cart'))
        if not item_found:
            print('{:^50}'.format('Item not found in cart. Nothing removed'))

    def modify_item(self, item_to_modify):  # item to purchase
        item_in_cart = False
        for item in self.cart_contents: 
            if item_to_modify.item_name == item.item_name:
                print('{:^50}'.format('Item ' + item.item_name + ' quantity changed from ' + str(item.item_quantity) + ' to ' + str(item_to_modify.item_quantity) + '.'))
                item.item_quantity = item_to_modify.item_quantity
                item_in_cart = True
        if not item_in_cart:
            print('{:^50}'.format('Item not found in cart. Nothing changed'))

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_contents:
            total_quantity += item.item_quantity
        return total_quantity
    
    def get_cost_of_cart(self):
        cost = 0
        for item in self.cart_contents:
            cost += item.item_price * item.item_quantity
        return cost
        
    def print_total(self):
        print('{:^50}'.format(self.customer_name + '\'s Shopping Cart - ' + self.current_date))
        if len(self.cart_contents) == 0:
            print('{:^50}'.format('SHOPPING CART IS EMPTY'))
        else:
            for item in self.cart_contents:
                item.print_item_cost()
            print('{:^50}'.format('Number of Items: ' + str(self.get_num_items_in_cart())))
            print('{:^50}'.format('${:,.2f}'.format(self.get_cost_of_cart())))

    def print_description(self):
        print('{:^50}'.format(self.customer_name + '\'s Shopping Cart - ' + self.current_date))
        print('{:^50}'.format('Item Descriptions'))
        if self.get_num_items_in_cart() == 0:
            print('{:^50}'.format('No items in cart'))
        else:
            for item in self.cart_contents:
                print('{:^50}'.format(item.item_name + ': ' + item.item_description))


def print_menu(cart):
    print('a - Add item to cart')
    print('r - Remove item from cart')
    print('c - Change item quantity')
    print('i - Output items\' descriptions')
    print('o - Output shopping cart')
    print('q - Quit')
    option = str(input('Choose an option: '))
    if option == 'q':
        return option
    elif option == 'a':
        print('{:^50}'.format('ADD ITEM TO CART'))
        item = ItemToPurchase()
        item.item_name = str(input('Enter the item name: '))
        item.item_price = float(input('Enter the item price: '))
        while not type(item.item_price) is float:
            item.item_price = float(input('Enter the item price in dollar and cents: '))
        item.item_quantity = int(input('Enter the item quantity: '))
        while not type(item.item_quantity) is int:
            item.item_quantity = int(input('Enter the item quantity in whole numbers: '))
        item.item_description = str(input('Enter the item description: '))
        if item.item_quantity > 0:
            cart.add_item(item)
        else:
            print('{:^50}'.format('Item quantity must be greater than 0.'))
            print('{:^50}'.format('Item not added to shopping cart.'))
    elif option == 'r':
        print('{:^50}'.format('REMOVE ITEM FROM CART'))
        item_name_to_remove = str(input('Enter the item name to remove: '))
        cart.remove_item(item_name_to_remove)
    elif option == 'c':
        print('{:^50}'.format('CHANGE ITEM QUANTITY'))
        item = ItemToPurchase()
        item.item_name = str(input('Enter the item name to modify: '))
        try:
            item.item_quantity = int(input('Enter new quantity: '))
        except ValueError:
            print('{:^50}'.format('Quantity number must be a whole number. Please try again.'))
        if item.item_quantity > 0:
            cart.modify_item(item)
        else:
            print('{:^50}'.format('Item quantity must be greater than 0.'))
            print('{:^50}'.format('Please try again or use remove option if item no longer needed.'))
            del item
    elif option == 'i':
        cart.print_description()
    elif option == 'o':
        cart.print_total()


customer_name = str(input('Enter customer name: ')).title()
while True:
    cart_date = input('Enter today\'s date: month day, year (ex. January 1, 2024): ')
    try:
        valid_date = datetime.strptime(cart_date, '%B %d, %Y')
        formatted_date = str(valid_date.strftime('%B %d, %Y'))
        break
    except ValueError:
        print('{:^50}'.format('Date is invalid, please enter valid date'))
print(f'Customer name: {customer_name}')
print(f'today\'s date: {cart_date}')

customer_cart = ShoppingCart(customer_name, formatted_date)
edit_cart = ""
while edit_cart != 'q':
    edit_cart = print_menu(customer_cart)

customer_cart.print_total()
customer_cart.print_description()
