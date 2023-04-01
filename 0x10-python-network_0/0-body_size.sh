#!/bin/bash
# get the size of the content of a web page
curl -s "$1" | wc -c
