# customer.py

#from order import Order  # Import Order class to use its methods

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Name must be between 1 and 15 characters")

    def orders(self):
        from order import Order
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        from order import Order
        non_unique = [order.coffee for order in Order.all if order.customer == self]
        unique = set(non_unique)
        return list(unique)

    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)
