import pandas as pd

# Загрузка данных из CSV-файла
df = pd.read_csv('olympics-economics.csv')

# Вывод первых 5 строк данных
print("Первые 5 строк данных:")
print(df.head())

# Вывод информации о данных
print("\nИнформация о данных:")
df.info()

# Вывод статистического описания
print("\nСтатистическое описание данных:")
print(df.describe())
