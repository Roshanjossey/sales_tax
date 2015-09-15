class ShoppingBasket(object):
    """ShoppingBasket instances has details about what contents are there
    in the shopping bakse

    contents - an array of  tuple of product instances, price and quantity of each product
    total_price_to_pay - float sum fo all prices
    total_sales_tax - float sum of all sales taxes added together"""

    def __init__(self):
        self.contents = []
        self.total_sales_tax = 0.0
        self.total_price_to_pay = 0.0

    def print_reciept(self):
        print 'Product     |              Total cost'
        for entry in self.contents:
            price, sales_tax = entry[0].price_and_tax()
            price *= entry[1]
            sales_tax *= entry[1]
            print '{}         |              {}'.format(entry[0].name, price)
            self.total_price_to_pay += price
            self.total_sales_tax += sales_tax
        print '--------------------------------'
        print 'Total price to pay :     ', self.total_price_to_pay
        print '--------------------------------'
        print 'Total sales tax :        ', self.total_sales_tax

    def add_entry(self, product, quantity):
        self.contents.append((product, quantity))