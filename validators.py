# Utils/validators.py
# HI-CAS - Automated Household Inventory & Intelligent Consumption Analytics System
# Module 2: Validation Module

def validate_quantity(q):
    if q < 0:
        raise ValueError("Quantity cannot be negative")
    return q

def validate_date(date):
    if date == "":
        raise ValueError("Invalid date")
    return date

def validate_name(name):
    if name.strip() == "":
        raise ValueError("Item name cannot be empty")
    return name

def validate_category(category):
    if category.strip() == "":
        raise ValueError("Category cannot be empty")
    return category
