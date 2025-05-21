import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

# 1.
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

tickers = ["GOOG", "SPY"]
data = yf.download(tickers, start=start_date, end=end_date)["Close"]
data.dropna(inplace=True)

# 2.
log_returns = np.log(data / data.shift(1)).dropna()

plt.figure(figsize=(12, 6))
log_returns.plot()
plt.title("Логарифмічна прибутковість GOOG та SPY")
plt.ylabel("Лог-прибутковість")
plt.grid(True)
plt.show()

# 3.
sample = log_returns.sample(n=60, random_state=42)

plt.figure(figsize=(8, 6))
sns.scatterplot(x=sample['SPY'], y=sample['GOOG'])
plt.title("Кореляція між лог-прибутковістю GOOG та SPY")
plt.xlabel("SPY")
plt.ylabel("GOOG")
plt.grid(True)
plt.show()

corr_coef = sample.corr().iloc[0, 1]
print(f"Коефіцієнт кореляції між GOOG та SPY: {corr_coef:.4f}")

# 4.
X = sample['SPY'].values.reshape(-1, 1)
y = sample['GOOG'].values.reshape(-1, 1)
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

plt.figure(figsize=(8, 6))
plt.scatter(X, y, label="Фактичні дані")
plt.plot(X, y_pred, color='red', label="Лінія регресії")
plt.title("Лінійна регресія GOOG від SPY")
plt.xlabel("SPY")
plt.ylabel("GOOG")
plt.legend()
plt.grid(True)
plt.show()

# 5.
spy_data = data['SPY'].copy()
spy_dates = np.arange(len(spy_data)).reshape(-1, 1)
spy_model = LinearRegression()
spy_model.fit(spy_dates, spy_data.values.reshape(-1, 1))
spy_trend = spy_model.predict(spy_dates)

plt.figure(figsize=(12, 6))
plt.plot(spy_data.index, spy_data, label="Ціна SPY")
plt.plot(spy_data.index, spy_trend, color='red', label="Лінія тренду")
plt.title("Тренд ціни SPY")
plt.xlabel("Дата")
plt.ylabel("Ціна")
plt.legend()
plt.grid(True)
plt.show()

# 6.
spy_recent = spy_data[-63:]
recent_days = np.arange(len(spy_recent)).reshape(-1, 1)
recent_model = LinearRegression()
recent_model.fit(recent_days, spy_recent.values.reshape(-1, 1))
trend_line = recent_model.predict(recent_days)
std_dev = np.std(spy_recent)

upper_band = trend_line.flatten() + std_dev
lower_band = trend_line.flatten() - std_dev

plt.figure(figsize=(12, 6))
plt.plot(spy_recent.index, spy_recent, label="SPY")
plt.plot(spy_recent.index, trend_line, color='red', label="Тренд")
plt.fill_between(spy_recent.index, lower_band, upper_band, color='gray', alpha=0.3, label="±1 Std Dev")
plt.title("SPY: Тренд та волатильність (ост. 63 дні)")
plt.legend()
plt.grid(True)
plt.show()

# 7.
def forecast_spy(days_ahead):
    future_day = np.array([[len(spy_data) + days_ahead]])
    return spy_model.predict(future_day)[0, 0]

# Приклад прогнозу
predicted_price = forecast_spy(10)
print(f"Прогнозована ціна SPY через 10 днів: {predicted_price:.2f}")
