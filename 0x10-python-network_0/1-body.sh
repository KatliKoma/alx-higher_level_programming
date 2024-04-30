#!/bin/bash
#This Bash script takes a URL as input, sends a request to it, and shows the size of the response body using curl.
curl -sX GET $1 -L
