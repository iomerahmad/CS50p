import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Invalid Usage")

try:
    float(sys.argv[1])
except ValueError:
    sys.exit("Please enter correct amount of BTC!") 

try:
    BTC = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=0f25252c0c4f1e0a5910f8c3d746e68a7522cfd9827f2f087b3f3e0c4211af42")
except requests.RequestException:
    pass

price = BTC.json()["data"]["priceUsd"]
final = float(sys.argv[1]) * float(price)

print(f"${final:,.4f}")
