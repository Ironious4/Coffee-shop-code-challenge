from customer import Customer 
from coffee import Coffee      
from order import Order        

def main():
    # Instantiate some customers
    customer1 = Customer("Bob")
    customer2 = Customer("Mosh")

    # Instantiate some coffees
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Latte")

    # Create some orders
    order1 = Order(customer1, coffee1, 2.5)
    order2 = Order(customer2, coffee1, 3.0)
    order3 = Order(customer1, coffee2, 4.5)

    # Print statements to display outputs

    # Customer details
    print("Customer 1 name:", customer1.name)
    print("Customer 1 orders:", [order.price for order in customer1.orders()])
    print("Customer 1 coffees:", [coffee.name for coffee in customer1.coffees()])

    print("Customer 2 name:", customer2.name)
    print("Customer 2 orders:", [order.price for order in customer2.orders()])
    print("Customer 2 coffees:", [coffee.name for coffee in customer2.coffees()])

    # Coffee details
    print("Coffee 1 name:", coffee1.name)
    print("Coffee 1 orders:", [order.price for order in coffee1.orders()])
    print("Coffee 1 customers:", [customer.name for customer in coffee1.customers()])
    print("Coffee 1 number of orders:", coffee1.num_orders())
    print("Coffee 1 average price:", coffee1.average_price())

    print("Coffee 2 name:", coffee2.name)
    print("Coffee 2 orders:", [order.price for order in coffee2.orders()])
    print("Coffee 2 customers:", [customer.name for customer in coffee2.customers()])
    print("Coffee 2 number of orders:", coffee2.num_orders())
    print("Coffee 2 average price:", coffee2.average_price())

    # Order details
    print("Order 1 details:")
    print("Customer:", order1.customer.name)
    print("Coffee:", order1.coffee.name)
    print("Price:", order1.price)

    print("Order 2 details:")
    print("Customer:", order2.customer.name)
    print("Coffee:", order2.coffee.name)
    print("Price:", order2.price)


if __name__ == "__main__":
    main()





