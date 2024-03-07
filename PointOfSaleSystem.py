class Saleltem:
  def __init__(self, item_id, name, unit_price):
    self.item_id = item_id
    self.name = name
    self.unit_price = unit_price

  def calculate_total(self, quantity):
    return self.unit_price * quantity

class StandardItem(Saleltem):
  def __init__(self, item_id, name, unit_price):
    super().__init__(item_id, name, unit_price)

  def calculate_total(self, quantity):
    return super().calculate_total(quantity)

class DiscountedItem(Saleltem):
  def __init__(self, item_id, name, unit_price, discount_percentage):
    super().__init__(item_id, name, unit_price)
    self.discount_percentage = discount_percentage

  def calculate_total(self, quantity):
    discounted_price = self.unit_price * (1 - self.discount_percentage / 100)
    return discounted_price * quantity

class ServiceItem(Saleltem):
  def __init__(self, item_id, name, hourly_rate):
    super().__init__(item_id, name, hourly_rate)
    self.hourly_rate = hourly_rate

  def calculate_total(self, hours):
    return self.hourly_rate * hours

# Example usage
standard_item = StandardItem(1, "T-shirt", 10.0)
discounted_item = DiscountedItem(2, "Hat", 20.0, 10)
service_item = ServiceItem(3, "Haircut", 50.0)

print(f"Standard item total: ${standard_item.calculate_total(2)}")
print(f"Discounted item total: ${discounted_item.calculate_total(1)}")
print(f"Service item total: ${service_item.calculate_total(2)}")
