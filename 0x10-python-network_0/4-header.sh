#!/bin/bash
# Retrieves and displays the response body of a curl request with a custom header.
curl -sH "X-HolbertonSchool-User-Id:98" "$1"
