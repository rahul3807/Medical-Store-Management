inventory = [
    {"name": "Paracetamol 650", "price": 15.0, "quantity": 50},
    {"name": "Dolo 650", "price": 30.0, "quantity": 8},
    {"name": "Combiflam", "price": 25.0, "quantity": 40},
    {"name": "Pantop 40", "price": 55.0, "quantity": 5}
]


def show_medicines():
    print("\nMedicine List")

    if not inventory:
        print("Stock is empty.")
        return

    print(f"{'Name':<20} | {'Price':>8} | {'Quantity':>8}")
    print("-" * 42)

    for item in inventory:
        print(f"{item['name']:<20} | Rs.{item['price']:>6.2f} | {item['quantity']:>8}")


def add_medicine():
    print("\nAdd Medicine")

    name = input("Enter medicine name: ").strip()

    if not name:
        print("Medicine name cannot be empty.")
        return

    try:
        price = float(input("Enter price: "))
        if price <= 0:
            print("Price must be greater than 0.")
            return

        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return
    except ValueError:
        print("Invalid input! Please enter numbers for price and quantity.")
        return

    # Check if medicine already exists
    for item in inventory:
        if item["name"].lower() == name.lower():
            item["quantity"] += quantity
            print("Stock updated successfully!")
            return

    # Add new medicine
    new_med = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    inventory.append(new_med)
    print("New medicine added!")