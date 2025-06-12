from json import dumps
from logging import error
from os import environ

# import debugpy  # Não esqueça de tirar pós testes
import pandas as pd
import yfinance as yf
from requests import get

# Não esqueça de tirar pós testes
# debugpy.listen(("0.0.0.0", 5678))
# print("⏳ Aguardando debugger...")
# debugpy.wait_for_client()
# ^^^ Não esqueça de tirar pós testes


def fetch_price_history(ticker: str, period: str = "5y"):
    try:
        stock = yf.Ticker(ticker)
        return stock.history(period=period)
    except Exception as e:
        error(f"Error fetching price history for {ticker}")
        raise e


def fetch_fundamentals(ticker: str) -> dict:
    param = {"token": environ.get("TOKEN_BRAPI")}
    response = get(f"https://brapi.dev/api/quote/{ticker}?range=1d", params=param)

    data = {
        "statusCode": response.status_code,
        "body": (
            response.json()["results"][0]
            if len(response.content) != 0
            else response.text
        ),
    }
    return data


def build_response(ticker: str, fundamentals: dict, history_df: pd.DataFrame) -> dict:
    price_history = [
        {"date": date.strftime("%Y-%m-%d"), "close": float(close)}
        for date, close in zip(history_df.index, history_df["Close"])
    ]

    return {
        "ticker": ticker,
        "fundamentals": fundamentals,
        "priceHistory": price_history,
    }


def handler(event: dict, context: dict):
    ticker_yf = "PETR4.SA"
    ticker_brapi = "PETR4"

    price_data = fetch_price_history(ticker_yf)
    response = fetch_fundamentals(ticker_brapi)
    if response["statusCode"] == 200:
        response = build_response(ticker_brapi, response["body"], price_data)
    return {"statusCode": 200, "body": dumps(response)}
