class Product(object):

    """docstring for Product"""

    def __init__(self, product_id, price, quantity):
        super(Product, self).__init__()
        self.id = product_id
        self.price = price
        self.quantity = quantity


class Inventory(object):

    """docstring for Inventory"""

    def __init__(self):
        super(Inventory, self).__init__()
        self.products = []

    def __add__(self, product):
        self.products.append(product)

    def get_inventory_value(self):
        return sum(item.price * item.quantity for item in self.products)


def add_product():
    product_id = raw_input("Enter product id:\n>>>")
    product_price = raw_input("Enter product price:\n>>>")
    product_quantity = raw_input("Enter product quantity:\n>>>")

    try:
        product_quantity = int(product_quantity)
        product_price = float(product_price)
    except:
        print "Invalid input, price and quantity have to be numerical values"
        return None

    if len(product_id) < 1:
        print "Invalid input, product id must be at least one char long"
        return None

    return Product(product_id, product_price, product_quantity)


if __name__ == '__main__':
    inventory = Inventory()
    while True:
        print "Pick an option\n1 - Add new product to inventory"
        print "2 - List current inventory value"
        user_choice = raw_input(">>>")
        if user_choice not in ["1", "2"]:
            print "invalid option"
        elif user_choice == "1":
            new_product = add_product()
            if new_product is not None:
                inventory.__add__(new_product)
        elif user_choice == "2":
            print "Inventory value:", inventory.get_inventory_value()
