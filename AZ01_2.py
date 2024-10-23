import pandas as pd

# Загрузка файла dz.csv в DataFrame
df = pd.read_csv('dz.csv')

# Рассчитываем среднюю зарплату по городам
avg_salary_by_city = df.groupby('City')['Salary'].mean()

# Выводим результат без метаданных
print(avg_salary_by_city.to_string())
