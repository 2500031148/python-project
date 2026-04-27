# Models/item.py
# HI-CAS - Automated Household Inventory & Intelligent Consumption Analytics System
# Module 1: Item Management Module

class Item:
    def __init__(self, name, category, quantity, min_stock, expiry):
        self._name = name
        self._category = category
        self._quantity = quantity
        self._min_stock = min_stock
        self._expiry = expiry

    def get_name(self):
        return self._name

    def get_category(self):
        return self._category

    def get_quantity(self):
        return self._quantity

    def update_quantity(self, amount):
        self._quantity += amount

    def is_low_stock(self):
        return self._quantity <= self._min_stock

    def get_expiry(self):
        return self._expiry

    def to_dict(self):
        return {
            "name": self._name,
            "category": self._category,
            "quantity": self._quantity,
            "min_stock": self._min_stock,
            "expiry": self._expiry
        }
