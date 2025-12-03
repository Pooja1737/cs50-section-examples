import sys
import requests
def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    try:
        API_KEY = "08e41a793ac6603515cdcbe2d2501462b1e12cf7d64c902d4b9fb8604fe965ed" 
        url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"
        response = requests.get(url)
        response.raise_for_status() 

        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Error fetching data")
    total = n * price
    print(f"{total:,.4f}")

if __name__ == "__main__":
    main()
