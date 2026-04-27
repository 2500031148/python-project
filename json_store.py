# Storage/json_store.py
# HI-CAS - Automated Household Inventory & Intelligent Consumption Analytics System
# Module 3: Storage Module

import json

FILE_NAME = "inventory.json"

def save_inventory(data):
    try:
        with open(FILE_NAME, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print("Error saving file:", e)

def load_inventory():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except:
        return []

def clear_inventory():
    save_inventory([])
