import json
import requests


def get_user_profile(user_id):
    """Fetches a specific mock user profile by ID from JSONPlaceholder."""
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException:
        pass
    return None


def get_crypto_prices():
    """Fetches live cryptocurrency prices from CoinGecko (No API key required)."""
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": "bitcoin,ethereum,solana", "vs_currencies": "usd"}
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException:
        pass
    return {}


def save_to_file(data, filename):
    """Saves the given data dictionary to a JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print(f"\n[Success] Portfolio report saved to '{filename}'")


def run_tool():
    print("=== Crypto Portfolio & Investor Tracker ===")
    print("------------------------------------------")

    # 1. Take user input
    user_input = input("Enter an investor ID (choose between 1 and 10): ").strip()
    
    if not user_input.isdigit():
        print("Invalid input. Please enter a valid number between 1 and 10.")
        return

    user_id = int(user_input)
    if user_id < 1 or user_id > 10:
        print("Investor ID out of range. Please choose a number between 1 and 10.")
        return

    print(f"\nFetching profile and live market data...")

    # 2. Make API calls
    user = get_user_profile(user_id)
    prices = get_crypto_prices()

    # 3. Handle error cases gracefully
    if not user:
        print(f"Error: Could not find investor profile with ID {user_id}.")
        return

    if not prices:
        print("Error: Could not retrieve live crypto market prices. Check your connection.")
        return

    # Extract live market prices
    btc_price = prices.get("bitcoin", {}).get("usd", 0)
    eth_price = prices.get("ethereum", {}).get("usd", 0)
    sol_price = prices.get("solana", {}).get("usd", 0)

    # Simulated asset holdings mapped to user IDs
    mock_holdings = {
        1: {"BTC": 0.5, "ETH": 4.0, "SOL": 20.0},
        2: {"BTC": 1.2, "ETH": 1.5, "SOL": 50.0},
        3: {"BTC": 0.1, "ETH": 10.0, "SOL": 5.0},
        4: {"BTC": 2.0, "ETH": 0.5, "SOL": 10.0},
        5: {"BTC": 0.3, "ETH": 8.0, "SOL": 15.0},
    }
    holdings = mock_holdings.get(user_id, {"BTC": 0.2, "ETH": 3.0, "SOL": 12.0})

    # Calculate portfolio values
    btc_val = holdings["BTC"] * btc_price
    eth_val = holdings["ETH"] * eth_price
    sol_val = holdings["SOL"] * sol_price
    total_value = btc_val + eth_val + sol_val

    # 4. Print clean, readable output for a non-technical user
    print(f"\n==========================================")
    print(f" INVESTOR PORTFOLIO REPORT")
    print(f"==========================================")
    print(f" Name    : {user['name']}")
    print(f" Email   : {user['email']}")
    print(f" Company : {user['company']['name']}")
    print(f"------------------------------------------")
    print(f" HOLDINGS & ASSET VALUE:")
    print(f" - Bitcoin (BTC)  : {holdings['BTC']} (${btc_val:,.2f})")
    print(f" - Ethereum (ETH) : {holdings['ETH']} (${eth_val:,.2f})")
    print(f" - Solana (SOL)   : {holdings['SOL']} (${sol_val:,.2f})")
    print(f"------------------------------------------")
    print(f" Total Net Worth  : ${total_value:,.2f}")
    print(f"==========================================")

    # Prepare data payload
    report_data = {
        "investor_name": user["name"],
        "email": user["email"],
        "holdings": holdings,
        "current_prices_usd": {"btc": btc_price, "eth": eth_price, "sol": sol_price},
        "total_portfolio_value_usd": total_value
    }

    # 5. Save response to a JSON file
    filename = f"{user['name'].split()[0].lower()}_portfolio.json"
    save_to_file(report_data, filename)


if __name__ == "__main__":
    run_tool()