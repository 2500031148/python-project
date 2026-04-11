import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



class Item:
    def __init__(self, name, category, quantity, expiry, min_stock):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.expiry = expiry
        self.min_stock = min_stock

    def update_quantity(self, amount):
        self.quantity += amount

    def is_low_stock(self):
        return self.quantity <= self.min_stock


# ---------------- FILE HANDLING ----------------
def save_data(data):
    with open("inventory.json", "w") as f:
        json.dump(data, f)


def load_data():
    try:
        with open("inventory.json", "r") as f:
            return json.load(f)
    except:
        return []


# ---------------- ADD ITEM ----------------
def add_item():
    try:
        name = input("Item name: ")
        category = input("Category: ")
        quantity = int(input("Quantity: "))
        expiry = input("Expiry date: ")
        min_stock = int(input("Minimum stock: "))

        item = Item(name, category, quantity, expiry, min_stock)

        data = load_data()
        data.append(item.__dict__)
        save_data(data)

        print("Item Added Successfully")

    except Exception as e:
        print("Error:", e)


# ---------------- VIEW ITEMS ----------------
def view_items():
    data = load_data()
    for item in data:
        print(item)


# ---------------- ANALYSIS (PANDAS) ----------------
def analyze():
    data = load_data()
    if len(data) == 0:
        print("No data")
        return

    df = pd.DataFrame(data)

    print("\nTotal Quantity:", df["quantity"].sum())

    print("\nCategory Wise:")
    print(df.groupby("category")["quantity"].sum())


# ---------------- FORECAST (NUMPY) ----------------
def forecast():
    data = load_data()
    quantities = [item["quantity"] for item in data]

    if len(quantities) == 0:
        print("No data")
        return

    avg = np.mean(quantities)
    print("Average Quantity:", avg)


# ---------------- CHART (MATPLOTLIB) ----------------
def show_chart():
    data = load_data()

    items = [i["name"] for i in data]
    quantities = [i["quantity"] for i in data]

    plt.bar(items, quantities)
    plt.title("Inventory Chart")
    plt.show()


# ---------------- MENU ----------------
while True:
    print("\nHI-CAS SYSTEM")
    print("1. Add Item")
    print("2. View Items")
    print("3. Analyze")
    print("4. Forecast")
    print("5. Show Chart")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_item()

    elif choice == "2":
        view_items()

    elif choice == "3":
        analyze()

    elif choice == "4":
        forecast()

    elif choice == "5":
        show_chart()

    elif choice == "6":
        break

    else:
        print("Invalid choice")
