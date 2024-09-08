class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if hasattr(self, "_name"):
            raise AttributeError("Coffee name cannot be changed")
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Coffee name must be at least 3 characters long")

    def orders(self):
        from order import Order
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        from order import Order
        all_customers = [order.customer for order in Order.all if order.coffee == self]
        unique_customers = set(all_customers)
        return list(unique_customers)

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        return sum([order.price for order in self.orders()]) / len(self.orders())
