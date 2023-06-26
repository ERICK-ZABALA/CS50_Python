
import requests
import sys

try:
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)
    if isinstance(float(sys.argv[1]), (int,float)):
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        amount = o['bpi']['USD']['rate_float']
        # print(o['bpi']['USD']['rate_float'])
        result = float(sys.argv[1]) * float(amount)
        print(f"${result:,.4f}")


except requests.RequestException:
    sys.exit(1)
except ValueError:
    print("Missing command-line argument")
    sys.exit(1)
except KeyError:
    sys.exit(1)