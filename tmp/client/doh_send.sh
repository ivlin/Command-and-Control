#/bin/bash

# Expected arguments: ./doh_send.sh FILE DESTINATION DOH_SERVER

curl --doh-url "$3" -H "Content-Type: application/octet-stream" --data @"$1" "$2"