#!/bin/bash

# Send GET request with silent mode and capture response
response=$(curl -s "$1")

# Check status code and display body if 200
if [[ $(echo "$response" | head -n 1) -eq 200 ]]; then
  echo "${response#*  }"  # Remove leading status code
fi
