#!/bin/bash

# Create the logs directory if it doesn't exist
mkdir -p /logs/verifier

# Run the test_outputs.py script
python3 /app/tests/test_outputs.py

# Write the reward based on the test result
if [ $? -eq 0 ]; then
    echo "1.0" > /logs/verifier/reward.txt
    echo "Test passed, reward written: 1.0"
else
    echo "0.0" > /logs/verifier/reward.txt
    echo "Test failed, reward written: 0.0"
fi
