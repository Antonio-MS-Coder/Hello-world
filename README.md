# Hello-world

Mi primer Repository

## CoinGecko Trending Script

This repository now includes a simple Python script that fetches trending cryptocurrency coins from the public CoinGecko API. Run it to see which coins are currently popular on the market.

### How to Use

1. Install the required dependency:

```bash
pip install requests
```

2. Execute the script:

```bash
python3 scripts/coin_trending.py
```

The output lists trending coins with their market cap ranking, name, and symbol.

**Disclaimer:** This script is for informational purposes only and does not constitute financial advice.

## Newsletter Site

The repository also contains a simple static website for a speculative crypto
newsletter. Open `site/index.html` directly in your browser or serve the
directory with a small web server:

```bash
python3 -m http.server --directory site
```

The page fetches trending coins from CoinGecko and includes a disclaimer that
the information is purely speculative and not financial advice.

## Deploying the Newsletter Site

You can host the static website using **GitHub Pages**. This repository already
contains a workflow that publishes the contents of the `site/` directory
whenever changes are pushed to `main`.

1. Ensure GitHub Pages is enabled in your repository settings and configured to
   deploy from GitHub Actions.
2. Push your changes to the `main` branch or trigger the workflow manually from
   the Actions tab.
3. Once the workflow succeeds, your newsletter will be available at the URL
   provided in the repository's Pages settings.

The included workflow file is located at
`.github/workflows/deploy.yml`.
