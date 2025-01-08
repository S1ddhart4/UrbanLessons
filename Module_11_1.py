import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Работа с pandas: Загрузка и анализ данных
# Загрузка данных из CSV-файла (создадим DataFrame вручную для демонстрации)
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 27, 22, 32],
    "Score": [85, 88, 92, 95]
}
df = pd.DataFrame(data)

# Показать первые строки данных
print("DataFrame (pandas):")
print(df)

# Основные статистические показатели
print("\nStatistics:")
print(df.describe())

# Фильтрация данных (Score > 90)
high_scores = df[df["Score"] > 90]
print("\nHigh Scores:")
print(high_scores)

# 2. Работа с numpy: Создание массива и операции
# Создание массива
array = np.array([1, 2, 3, 4, 5])
print("\nNumpy Array:", array)

# Операции с массивом
array_squared = array ** 2
print("Squared Array:", array_squared)

# Генерация случайного массива и вычисление среднего
random_array = np.random.rand(5)
print("Random Array:", random_array)
print("Mean of Random Array:", np.mean(random_array))

# 3. Работа с matplotlib: Визуализация данных
# Построение линейного графика
plt.figure(figsize=(8, 5))
plt.plot(df["Name"], df["Score"], marker="o", label="Score")
plt.title("Scores of Students")
plt.xlabel("Name")
plt.ylabel("Score")
plt.legend()
plt.grid()
plt.show()

# Построение гистограммы
plt.figure(figsize=(8, 5))
plt.hist(array_squared, bins=5, color="skyblue", edgecolor="black")
plt.title("Histogram of Squared Values")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()