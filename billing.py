from medicines import inventory


def make_bill():
    print("\nBilling System")

    if not inventory:
        print("No stock available.")
        return

    total = 0
    bill_list = []

    while True:
        med_name = input(
            "Enter medicine name to buy (or type 'done' to stop): "
        ).strip()

        if med_name.lower() == "done":
            break

        found = False

        for item in inventory:
            if item["name"].lower() == med_name.lower():
                found = True

                # Check how many are already added to this bill
                already_in_bill = sum(
                    b["qty"] for b in bill_list if b["item"] is item
                )
                available = item["quantity"] - already_in_bill

                while True:
                    try:
                        qty = int(input("Enter quantity: "))
                    except ValueError:
                        print("Invalid quantity! Please enter a number.")
                        continue

                    if qty <= 0:
                        print("Quantity must be greater than 0.")
                        continue

                    if qty > available:
                        print("Not enough stock! Available:", available)
                        continue

                    break

                cost = qty * item["price"]
                total += cost

                bill_list.append({
                    "item": item,
                    "name": item["name"],
                    "qty": qty,
                    "cost": cost
                })

                print("Added to bill.")
                break

        if not found:
            print("Medicine not found in inventory!")

    # Print final bill
    if not bill_list:
        print("No items purchased.")
        return

    print("\n" + "=" * 30)
    print("          FINAL BILL")
    print("=" * 30)

    for b in bill_list:
        print(f"{b['name']} x {b['qty']} = Rs. {b['cost']:.2f}")

    print("-" * 30)
    print(f"Total Amount: Rs. {total:.2f}")
    print("=" * 30)

    # Confirm before reducing stock
    confirm = input("Confirm purchase? (yes/no): ").strip().lower()

    if confirm == "yes":
        for b in bill_list:
            b["item"]["quantity"] -= b["qty"]
        print("Purchase successful! Stock updated.")
    else:
        print("Purchase cancelled. Stock not updated.")


if __name__ == "__main__":
    make_bill()