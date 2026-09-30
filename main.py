from medicines import show_medicine , add_medicine
from billing import make_bill
from inventory import check_low_stock


def display_menu():
    print("\n" + "=" * 30)
    print("      MEDICAL STORE SYSTEM")
    print("=" * 30)
    print("1. View Medicines")
    print("2. Add Medicine")
    print("3. Create Bill")
    print("4. Check Low Stock")
    print("5. Exit")


def main():
    while True:
        display_menu()

        try:
            choice = input("Enter option (1-5): ").strip()

        except (EOFError, KeyboardInterrupt):
            print("\nProgram interrupted. Exiting...")
            break

        if choice == "1":
            show_medicines()

        elif choice == "2":
            add_medicine()

        elif choice == "3":
            make_bill()

        elif choice == "4":
            check_low_stock()

        elif choice == "5":
            print("Thank you! Exiting program...")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()