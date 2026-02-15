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
    """Test that each object has only id, name, and city fields"""
    required_fields = {"id", "name", "city"}
    for i, item in enumerate(data):
        fields = set(item.keys())
        assert fields == required_fields, f"Item {i} has extra or missing fields: {fields}"
    print("✓ All items have required fields (id, name, city)")

def test_output_values_are_correct(data):
    """Test that the values are correctly transformed"""
    expected_ids = [1, 2, 3, 4, 5]
    expected_names = ["John Doe", "Jane Smith", "Bob Johnson", "Alice Williams", "Charlie Brown"]
    expected_cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
    
    for i, item in enumerate(data):
        assert item["id"] == expected_ids[i], f"Item {i} has wrong id: {item['id']}"
        assert item["name"] == expected_names[i], f"Item {i} has wrong name: {item['name']}"
        assert item["city"] == expected_cities[i], f"Item {i} has wrong city: {item['city']}"
    
    print("✓ All values are correctly transformed")

def main():
    try:
        test_output_exists()
        data = test_output_is_valid_json()
        test_output_has_correct_structure(data)
        test_output_has_required_fields(data)
        test_output_values_are_correct(data)
        
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
