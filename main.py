import re
from product import Product
from shopping_basket import ShoppingBasket


cart = ShoppingBasket()  # A list to store all products in the basket
while 1:
    print 'Enter product details, enter "done" to finish : '
    product_details = raw_input()
    if product_details == 'done':
        break
    product_re = re.compile(r'(\d+) ([\w ]+) at (\d+(\.\d{1,2})?)')
    product_details = product_re.match(product_details)
    quantity = int(product_details.group(1))
    product_name = product_details.group(2)
    price = float(product_details.group(3))
    print '\nEnter coma seperated tags: '
    tags = raw_input()
    tags = tags.split(',')
    product = Product(product_name, price, tags)
    cart.add_entry(product, quantity)

cart.print_reciept()