"""
import sys
import requests


def main():
    if len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
            print(btc_price(n))
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")


def btc_price(num):
    try:
        response = requests.get(f"https://api.coindesk.com/v1/bpi/currentprice.json")
        result = response.json()
        price = result["bpi"]["USD"]["rate_float"]
        total = price * num
        return f"${total:,.4f}"
    except requests.RequestException:
        return None


main()
"""



import sys
import requests

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
    bitcoin = response['bpi']['USD']['rate_float']
    total_amount = bitcoin * value
    print(f'${total_amount:,.4f}')

except requests.RequestException:
    print("RequestException")
    sys.exit(1)
