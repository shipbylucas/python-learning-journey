import json
import requests
import sys


if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
else:
    try:
        num = float(sys.argv[1])
        coincap = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=a0501d307cc58b10749efc63317abbf1d697e4ba35a432dddf23dbbc849da533")
        price = coincap.json()
        ans = num * float(price["data"]["priceUsd"])
        print(f"${ans:,.4f}", end="")
    except NameError:
        sys.exit("Command-line argument is not a number")
