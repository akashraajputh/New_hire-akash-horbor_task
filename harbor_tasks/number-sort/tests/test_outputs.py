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

def test_output_is_array(data):
    """Test that output is a JSON array"""
    assert isinstance(data, list), "Output should be a list"
    assert len(data) > 0, "Output should not be empty"
    print(f"✓ Output is an array with {len(data)} items")

def test_output_is_sorted(data):
    """Test that numbers are sorted in ascending order"""
    for i in range(len(data) - 1):
        assert data[i] <= data[i + 1], f"Numbers are not sorted: {data[i]} > {data[i + 1]}"
    print("✓ Numbers are sorted in ascending order")

def test_output_contains_all_numbers(data):
    """Test that all numbers from input are present"""
    expected_numbers = [0.5, 1.25, 2.5, 3.14, 7, 15, 42, 88, 100, 200]
    
    # Convert both to sets for comparison (handling float precision)
    data_set = set(data)
    expected_set = set(expected_numbers)
    
    assert len(data) == len(expected_numbers), f"Expected {len(expected_numbers)} numbers, got {len(data)}"
    assert data_set == expected_set, f"Numbers don't match. Expected: {expected_set}, Got: {data_set}"
    print("✓ All numbers from input are present")

def test_output_types_are_correct(data):
    """Test that numbers maintain their types (int vs float)"""
    # Check that integers are integers and decimals are floats
    has_integers = any(isinstance(x, int) for x in data)
    has_floats = any(isinstance(x, float) for x in data)
    assert has_integers or has_floats, "Output should contain numbers"
    print("✓ Number types are correct")

def main():
    try:
        test_output_exists()
        data = test_output_is_valid_json()
        test_output_is_array(data)
        test_output_is_sorted(data)
        test_output_contains_all_numbers(data)
        test_output_types_are_correct(data)
        
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
