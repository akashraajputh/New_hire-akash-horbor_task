#!/usr/bin/env python3

import json
import os
import sys

def test_output_exists():
    """Test that output.json file exists"""
    assert os.path.exists("/app/output.json"), "output.json not found"
    print("✓ output.json exists")

def test_output_is_valid_json():
    """Test that output.json is valid JSON"""
    try:
        with open("/app/output.json", "r") as f:
            data = json.load(f)
        print("✓ output.json is valid JSON")
        return data
    except json.JSONDecodeError as e:
        assert False, f"output.json is not valid JSON: {e}"

def test_output_has_correct_structure(data):
    """Test that output has correct structure (array of objects)"""
    assert isinstance(data, list), "Output should be a list"
    assert len(data) > 0, "Output should not be empty"
    print(f"✓ Output has {len(data)} items")

def test_output_has_required_fields(data):
    """Test that each object has name, price, and category fields"""
    required_fields = {"name", "price", "category"}
    for i, item in enumerate(data):
        fields = set(item.keys())
        assert fields == required_fields, f"Item {i} has extra or missing fields: {fields}"
    print("✓ All items have required fields (name, price, category)")

def test_prices_are_numbers(data):
    """Test that price values are numbers, not strings"""
    for i, item in enumerate(data):
        assert isinstance(item["price"], (int, float)), f"Item {i} price is not a number: {type(item['price'])}"
    print("✓ All prices are numbers")

def test_filtering_applied(data):
    """Test that all products have price >= 50.0"""
    for i, item in enumerate(data):
        assert item["price"] >= 50.0, f"Item {i} has price < 50.0: {item['price']}"
    print("✓ All products have price >= 50.0")

def test_sorting_applied(data):
    """Test that products are sorted by price in ascending order"""
    prices = [item["price"] for item in data]
    assert prices == sorted(prices), "Products are not sorted by price in ascending order"
    print("✓ Products are sorted by price (ascending)")

def test_correct_products_included(data):
    """Test that the correct products are included"""
    # Expected products with price >= 50.0, sorted by price
    expected_products = [
        {"name": "Keyboard", "price": 75.0, "category": "Electronics"},
        {"name": "Printer", "price": 199.99, "category": "Electronics"},
        {"name": "Monitor", "price": 299.99, "category": "Electronics"},
        {"name": "Desk", "price": 350.0, "category": "Furniture"},
        {"name": "Tablet", "price": 450.0, "category": "Electronics"},
        {"name": "Laptop", "price": 999.99, "category": "Electronics"}
    ]
    
    assert len(data) == len(expected_products), f"Expected {len(expected_products)} products, got {len(data)}"
    
    for i, (actual, expected) in enumerate(zip(data, expected_products)):
        assert actual["name"] == expected["name"], f"Item {i} name mismatch: {actual['name']} != {expected['name']}"
        assert abs(actual["price"] - expected["price"]) < 0.01, f"Item {i} price mismatch: {actual['price']} != {expected['price']}"
        assert actual["category"] == expected["category"], f"Item {i} category mismatch: {actual['category']} != {expected['category']}"
    
    print("✓ Correct products are included and sorted")

def main():
    try:
        test_output_exists()
        data = test_output_is_valid_json()
        test_output_has_correct_structure(data)
        test_output_has_required_fields(data)
        test_prices_are_numbers(data)
        test_filtering_applied(data)
        test_sorting_applied(data)
        test_correct_products_included(data)
        
        print("\n✅ All tests passed!")
        sys.exit(0)
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
