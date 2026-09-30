# Inventory management

from medicines import inventory


def check_low_stock(threshold=10):
    print("\nLow Stock Alert")

    if not inventory:
        print("No items in inventory.")
        return

    found_any = False

    for item in inventory:
        name = item.get("name", "Unknown")
        qty = item.get("quantity", 0)

        if qty < threshold:
            print(f"ALERT: {name} - Only {qty} left!")
            found_any = True

    if not found_any:
        print("All items have enough stock.")