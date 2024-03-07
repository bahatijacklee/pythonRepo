from abc import ABC, abstractmethod
from datetime import datetime

class Product(ABC):
    def __init__(self, product_id, name, quantity_in_stock):
        self.product_id = product_id
        self.name = name
        self.quantity_in_stock = quantity_in_stock

    def get_product_id(self):
        return self.product_id

    def get_name(self):
        return self.name

    def get_quantity_in_stock(self):
        return self.quantity_in_stock

    def set_quantity_in_stock(self, new_quantity):
        self.quantity_in_stock = new_quantity

    @abstractmethod
    def calculate_value(self):
        pass

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Quantity in Stock: {self.quantity_in_stock}"
class SimpleProduct(Product):
    def __init__(self, product_id, name, quantity_in_stock, unit_price):
        super().__init__(product_id, name, quantity_in_stock)
        self.unit_price = unit_price

    def calculate_value(self):
        return self.unit_price * self.quantity_in_stock


    class PerishableProduct(Product):
        def __init__(self, product_id, name, quantity_in_stock, unit_price, expiry_date):
            super().__init__(product_id, name, quantity_in_stock)
            self.unit_price = unit_price
            self.expiry_date = expiry_date

        def calculate_value(self):
            remaining_shelf_life = (self.expiry_date - datetime.now()).days
            discount_rate = 0.1  # Example discount rate
            if remaining_shelf_life <= 0:
                return 0  # If the product is expired, its value is zero
            else:
                return (1 - discount_rate) * self.unit_price * self.quantity_in_stock

    class DigitalProduct(Product):
        def __init__(self, product_id, name, quantity_in_stock, price):
            super().__init__(product_id, name, quantity_in_stock)
            self.price = price

        def calculate_value(self):
            return self.price * self.quantity_in_stock

    # Example usage:
    if __name__ == "__main__":
        # Creating an instance of DigitalProduct
        digital_product = DigitalProduct(3, "Software", 5, 50)

        # Accessing attributes
        print("Product ID:", digital_product.get_product_id())
        print("Name:", digital_product.get_name())
        print("Quantity in Stock:", digital_product.get_quantity_in_stock())
        print("Price:", digital_product.price)

        # Calculating total value
        print("Total Value:", digital_product.calculate_value())
