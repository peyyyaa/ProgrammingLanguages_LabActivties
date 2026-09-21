class Item:

    def __init__(self, name, quantity, price):
        name = str(name).strip()
        if not name:
            raise ValueError("Item name cannot be empty.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a whole number, 0 or more.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price cannot be negative.")

        self.name = name
        self.__quantity = quantity   
        self.__price = float(price)  

    @property
    def quantity(self):
        return self.__quantity

    @property
    def price(self):
        return self.__price

    def restock(self, qty):
        if not isinstance(qty, int) or qty <= 0:
            print("  Restock rejected: quantity must be a positive whole number.")
            return False
        self.__quantity += qty
        print(f"  Restocked {qty} x {self.name}. New quantity: {self.__quantity}")
        return True

    def sell(self, qty):
        if not isinstance(qty, int) or qty <= 0:
            print("  Sale rejected: quantity must be a positive whole number.")
            return False
        if qty > self.__quantity:
            print(f"  Sale rejected: only {self.__quantity} in stock, "
                  f"cannot sell {qty}.")
            return False
        self.__quantity -= qty
        print(f"  Sold {qty} x {self.name}. Remaining quantity: {self.__quantity}")
        return True

    def total_value(self):
        return self.__quantity * self.__price

    def display(self):
        print(f"  Item: {self.name}")
        print(f"    Quantity    : {self.quantity}")
        print(f"    Price       : PHP {self.price:,.2f}")
        print(f"    Total value : PHP {self.total_value():,.2f}")


class PerishableItem(Item):

    DISCOUNT = 0.50         
    EXPIRY_THRESHOLD = 3     

    def __init__(self, name, quantity, price, days_until_expiry):
        super().__init__(name, quantity, price)
        if not isinstance(days_until_expiry, int) or days_until_expiry < 0:
            raise ValueError("Days until expiry must be a whole number, 0 or more.")
        self.days_until_expiry = days_until_expiry

    def is_expiring_soon(self):
        return self.days_until_expiry <= self.EXPIRY_THRESHOLD

    def total_value(self):
        value = super().total_value()
        if self.is_expiring_soon():
            value *= (1 - self.DISCOUNT)
        return value

    def display(self):
        super().display()
        print(f"    Expires in  : {self.days_until_expiry} day(s)")
        if self.is_expiring_soon():
            print(f"    NOTE        : Expiring soon - {int(self.DISCOUNT * 100)}% "
                  f"discount applied to total value")


class ElectronicItem(Item):

    def __init__(self, name, quantity, price, warranty_months):
        super().__init__(name, quantity, price)
        if not isinstance(warranty_months, int) or warranty_months < 0:
            raise ValueError("Warranty must be a whole number of months, 0 or more.")
        self.warranty_months = warranty_months

    def display(self):
        super().display()
        print(f"    Warranty    : {self.warranty_months} month(s)")
