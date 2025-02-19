import requests as req
import pandas as pd
import sqlite3


url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "ids": "bitcoin,ethereum,dogecoin",
    "order": "market_cap_desc",
    "per_page": 100,
    "page": 1,
    "sparkline": False
}

res = req.get(url, params=params)

data = res.json()

df = pd.DataFrame(data)

df = df[["id", "symbol", "name", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"]]

df.columns = ["ID", "Mã", "Tên", "Giá Hiện Tại (USD)", "Vốn Hóa Thị Trường", "Tổng Khối Lượng Giao Dịch", "Biến Động 24h (%)"]

tang_gia = df[df["Biến Động 24h (%)"] > 0.2]

# connect to sql
conn = sqlite3.connect("crypto_data.db")

# save data to sql
df.to_sql("crypto_prices", conn, if_exists="replace", index=False)

# read data from sql
df_sql = pd.read_sql("SELECT * FROM crypto_prices", conn)
# print(df_sql)


# get data from binance
binance_url = "https://api.binance.com/api/v3/ticker/price"
symbols = ["BTCUSDT", "ETHUSDT", "DOGEUSDT"]

crypto_prices = []
for symbol in symbols:
    response = req.get(binance_url, params={"symbol": symbol})
    data = response.json()
    crypto_prices.append({"Mã": symbol, "Giá Hiện Tại (USD)": float(data["price"])})

# convert to dataframe
df_binance = pd.DataFrame(crypto_prices)

name_mapping = {
    "BTCUSDT": "btc",
    "ETHUSDT": "eth",
    "DOGEUSDT": "doge"
}

df_binance["Mã"] = df_binance["Mã"].map(name_mapping)

# print(df_binance)

df_merged = df.merge(df_binance, on="Mã", how="outer")

print(df_merged)

# save to csv
df_merged.to_csv("./pandas/project3/crypto_prices.csv", index=False)
