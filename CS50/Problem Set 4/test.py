import requests
import sys

if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")

else:
    print("missing command-line argument")
    sys.exit(1)

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response = r.json()

except requests.RequestException:
    ...