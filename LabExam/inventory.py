from items import Item
class Inventory:
    def __init__(self):
        self.items = []

    def search(self, name):
        target = str(name).strip().lower()
        for item in self.items:
            if item.name.lower() == target:
                return item
        return None
    
    def update_quantity(self, name, qty):
        item = self.search(name)
        if item is None:
            print(f"  Item '{name}' not found.")
            return False
        return item.restock(qty)
    
    def add_item(self, item):
        if not isinstance(item, Item):
            print("  Cannot add: not a valid item.")
            return False
        if self.search(item.name) is not None:
            print(f"  Cannot add: '{item.name}' already exists in the inventory.")
            return False
        self.items.append(item)
        print(f"  '{item.name}' added to the inventory.")
        return True

    def total_inventory_value(self):
        return sum(item.total_value() for item in self.items)

    def sell_item(self, name, qty):
        item = self.search(name)
        if item is None:
            print(f"  Item '{name}' not found.")
            return False
        return item.sell(qty)

    def display_all(self):
        if not self.items:
            print("  The inventory is empty.")
            return
        print(f"  --- Inventory ({len(self.items)} item(s)) ---")
        for item in self.items:
            item.display()   
            print()

