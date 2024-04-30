#!/bin/bash

# Function to check status code and display body
display_body_if_success() {
  local status_code="$1"
  local body="$2"

  if [[ $status_code -eq 200 ]]; then
    echo "$body"
  fi
}

# Get the URL from the first argument
url="$1"

# Send GET request with silent mode and capture response in a variable
response=$(curl -s -o /dev/null -w "%{http_code}" "$url")

# Extract status code and body
status_code="${response##* }"
body="${response%[^ ]*}"  # Remove trailing status code

# Call function to display body only for success (status code 200)
display_body_if_success "$status_code" "$body"
