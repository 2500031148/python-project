# Analysis/analyzer.py
# HI-CAS - Automated Household Inventory & Intelligent Consumption Analytics System
# Module 4: Analysis Module

import pandas as pd

def consumption_summary(data):
    if len(data) == 0:
        return 0
    df = pd.DataFrame(data)
    return df["quantity"].sum()

def category_group(data):
    if len(data) == 0:
        return {}
    df = pd.DataFrame(data)
    return df.groupby("category")["quantity"].sum()

def low_stock_items(data):
    if len(data) == 0:
        return []
    df = pd.DataFrame(data)
    low = df[df["quantity"] <= df["min_stock"]]
    return low
