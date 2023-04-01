#!/bin/bash
# sends a POST request to agiven URL, and displays the body of the response
curl -sL -X POST -d 'email=test%40gmail.com&subject=I+will+always+be+here+for+PLD' "$1"
