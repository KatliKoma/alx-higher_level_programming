#!/bin/bash
# Retrieves and displays the HTTP status code size from the response of a curl request
curl -so /dev/null -w '%{http_code}' "$1"
