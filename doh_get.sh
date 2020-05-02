#/bin/bash

# Expected arguments: ./get_keys.sh URL

curl --doh-url dns.google.com "$1"	