class Product(object):
    """Product instances store details of products

    attributes
      name: name of product
      price: price
      imported: Whether product is imported or not
      sales_tax_applicable: Whether sales tax is applicable to product or not"""
    tags_tax = {'book': 0.0, 'food': 0.0, 'medical product': 0.0, 'imported': 0.05}

    def __init__(self, name, price, tags):
        self.name = name
        self.price = price
        self.tags = tags
        self.total_tax = 0.0
        for tag in tags:
            if tag in self.tags_tax:
                self.total_tax += self.tags_tax[tag]

    def price_and_tax(self):
        price = self.price * (1 + self.total_tax)
        sales_tax = self.price * self.total_tax
        return price, sales_tax
        