#!/bin/bash

# Check if URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request to URL and store response in a temporary file
response=$(curl -s -w "%{size_download}" -o /dev/null "$1")

# Display the size of the body of the response
echo "$response"

