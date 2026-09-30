# Medical Store Management System

A simple Python-based Medical Store Management System for managing medicines, inventory, billing, and low-stock alerts.

## Project Description

The Medical Store Management System is a console-based Python application designed to perform basic medical store operations.

The application allows the user to:

- View available medicines
- Add new medicines
- Update stock of existing medicines
- Create customer bills
- Check available stock before billing
- Confirm or cancel purchases
- Check medicines with low stock
- Handle invalid user input

## Features

### 1. View Medicines

Displays all medicines currently available in the inventory along with:

- Medicine name
- Price
- Quantity

### 2. Add Medicine

Allows the user to add a new medicine to the inventory.

If the medicine already exists, the program increases its stock quantity instead of creating a duplicate entry.

### 3. Create Bill

The billing system allows the user to:

- Select medicines by name
- Enter the required quantity
- Check available stock
- Calculate the cost
- Add multiple medicines to a bill
- Display the final bill
- Confirm or cancel the purchase

Stock is updated only after the purchase is confirmed.

### 4. Low Stock Alert

The system checks the inventory and displays an alert for medicines whose quantity is below the low-stock threshold.

The default threshold is 10 units.

### 5. Input Validation

The application validates user input for:

- Empty medicine names
- Invalid prices
- Invalid quantities
- Zero or negative quantities
- Quantity greater than available stock
- Invalid menu choices

## Project Structure

```text
Medical Store Management/
│
├── main.py
├── medicines.py
├── billing.py
├── inventory.py
├── README.md
└── .gitignore
