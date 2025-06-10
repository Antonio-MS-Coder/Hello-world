import requests

COINGECKO_TRENDING_URL = "https://api.coingecko.com/api/v3/search/trending"


def fetch_trending():
    response = requests.get(COINGECKO_TRENDING_URL, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data.get("coins", [])


def format_coin(coin_entry):
    item = coin_entry.get("item", {})
    name = item.get("name")
    symbol = item.get("symbol")
    market_cap_rank = item.get("market_cap_rank")
    return f"{market_cap_rank:>4}: {name} ({symbol})"


if __name__ == "__main__":
    print("Trending Coins on CoinGecko:\n")
    try:
        trending_list = fetch_trending()
        for coin in trending_list:
            print(format_coin(coin))
    except requests.HTTPError as e:
        print(f"HTTP error: {e}")
    except Exception as e:
        print(f"Error: {e}")
