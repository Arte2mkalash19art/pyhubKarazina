import pandas as pd

temperatures = [12, 15, 20, 10, 9, 15, 14]
days = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'Пʼятниця', 'Субота', 'Неділя']

tem_series = pd.Series(temperatures, index=days)

max_temp = tem_series.max()
min_temp = tem_series.min()

max_days = tem_series[tem_series == max_temp].index.tolist()
min_days = tem_series[tem_series == min_temp].index.tolist()

avg_temp = tem_series.mean()
stats = tem_series.describe()
print("Прогноз температури на тиждень:")
print(tem_series)
print("\nНайбільша температура:", max_temp, "°C, у дні:", ', '.join(max_days))
print("Найменша температура:", min_temp, "°C, у дні:", ', '.join(min_days))
print("Середня температура за тиждень:", round(avg_temp, 2), "°C")
print("\nСтатистичні характеристики:")
print(stats)