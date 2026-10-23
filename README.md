# Crypto Portfolio Tracker

A command line tool that combines investor profile data with real-time cryptocurrency market prices to track asset valuations and export audit reports.

## What It Does

- Accepts an investor ID through interactive user input
- Fetches client details securely from the JSONPlaceholder API
- Pulls live crypto prices (Bitcoin, Ethereum, Solana) from CoinGecko without requiring an API key
- Calculates total portfolio net worth based on simulated holdings
- Saves the generated summary report to a local JSON file
- Handles connection errors and invalid user input gracefully

## Setup

Requires Python 3.10 or newer.

Install the dependencies:

```bash
python -m pip install requests 
```

## usage

Run the script from your terminal::

```bash
python "crypto_investor_tool.py"
```
Enter an investor ID between 1 and 10 when prompted.

## sample output.

```text
==========================================
 INVESTOR PORTFOLIO REPORT
==========================================
 Name    : Glenna Reichert
 Email   : Chaim_McDermott@dana.io
 Company : Romaguera-Crona
------------------------------------------
 HOLDINGS & ASSET VALUE:
 Bitcoin (BTC)  : 0.5 ($34,500.00)
 Ethereum (ETH) : 4.0 ($12,000.00)
 Solana (SOL)   : 20.0 ($3,000.00)
------------------------------------------
 Total Net Worth  : $49,500.00
==========================================

[Success] Portfolio report saved to 'Glenna_portfolio.json'
```
## stack

Python, Requests, JSONPlaceholder API, CoinGecko API
