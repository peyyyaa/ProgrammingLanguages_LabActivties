from items import Item, PerishableItem, ElectronicItem
from inventory import Inventory

def read_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  Input cannot be empty. Try again.")

def read_int(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("  Please enter a whole number.")

def read_float(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
            if value != value or value in (float("inf"), float("-inf")):
                raise ValueError
            return value
        except ValueError:
            print("  Please enter a valid number.")


def add_item_menu(inventory):
    print("\n  Item type:")
    print("    1. General item")
    print("    2. Perishable item")
    print("    3. Electronic item")
    kind = input("  Choose type (1-3): ").strip()
    if kind not in ("1", "2", "3"):
        print("  Invalid type.")
        return

    name = read_text("  Item name: ")
    if inventory.search(name) is not None:   
        print(f"  Cannot add: '{name}' already exists in the inventory.")
        return
    quantity = read_int("  Quantity: ")
    price = read_float("  Price: ")

    try:
        if kind == "1":
            item = Item(name, quantity, price)
        elif kind == "2":
            days = read_int("  Days until expiry: ")
            item = PerishableItem(name, quantity, price, days)
        else:
            months = read_int("  Warranty (months): ")
            item = ElectronicItem(name, quantity, price, months)
    except ValueError as error:
        print(f"  Could not create item: {error}")
        return

    inventory.add_item(item)

def restock_menu(inventory):
    name = read_text("  Item name to restock: ")
    if inventory.search(name) is None:
        print(f"  Item '{name}' not found.")
        return
    qty = read_int("  Quantity to add: ")
    inventory.update_quantity(name, qty)

def sell_menu(inventory):
    name = read_text("  Item name to sell: ")
    if inventory.search(name) is None:
        print(f"  Item '{name}' not found.")
        return
    qty = read_int("  Quantity to sell: ")
    inventory.sell_item(name, qty)

def search_menu(inventory):
    name = read_text("  Item name to search: ")
    item = inventory.search(name)
    if item is None:
        print(f"  Item '{name}' not found.")
    else:
        item.display()

def show_menu():
    print("\n𐙚 ‧₊˚ ⋅ INVENTORY SYSTEM 𐙚 ‧₊˚ ⋅")
    print("  1. Add item")
    print("  2. Restock")
    print("  3. Sell")
    print("  4. Search")
    print("  5. Display all items")
    print("  6. Show total inventory value")
    print("  7. Exit\n")

def main():
    inventory = Inventory()

    while True:
        show_menu()
        try:
            choice = input("Choose an option (1-7): ").strip()

            if choice == "1":
                add_item_menu(inventory)
            elif choice == "2":
                restock_menu(inventory)
            elif choice == "3":
                sell_menu(inventory)
            elif choice == "4":
                search_menu(inventory)
            elif choice == "5":
                print()
                inventory.display_all()
            elif choice == "6":
                print(f"  Total inventory value: "
                      f"PHP {inventory.total_inventory_value():,.2f}")
            elif choice == "7":
                print("  Goodbye!")
                break
            else:
                print("  Invalid option. Please choose 1-7.")
        except (KeyboardInterrupt, EOFError):
            print("\n  Input closed. Exiting program.")
            break


if __name__ == "__main__":
    main()
