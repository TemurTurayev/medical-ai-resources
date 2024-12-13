import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Создаём тестовые данные пациентов
data = {
    'age': [45, 52, 38, 61, 43, 57, 29, 51, 33, 47],
    'gender': ['M', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'F'],
    'blood_pressure': [132, 141, 125, 153, 138, 145, 118, 142, 127, 136],
    'cholesterol': [213, 245, 198, 267, 223, 234, 187, 256, 201, 225],
    'heart_disease': [0, 1, 0, 1, 0, 1, 0, 1, 0, 0]
}

# Создаём DataFrame
df = pd.DataFrame(data)

# 1. Базовый анализ
print("Основная статистика:")
print(df.describe())

print("\nПроверка пропущенных значений:")
print(df.isnull().sum())

# 2. Анализ распределений
print("\nРаспределение по полу:")
print(df['gender'].value_counts())

print("\nСредние значения по полу:")
print(df.groupby('gender').mean())

# 3. Визуализация
plt.figure(figsize=(12, 6))

# График зависимости давления от возраста
plt.subplot(1, 2, 1)
plt.scatter(df['age'], df['blood_pressure'], c=df['heart_disease'], cmap='coolwarm')
plt.xlabel('Возраст')
plt.ylabel('Давление')
plt.title('Зависимость давления от возраста')

# Распределение холестерина по полу
plt.subplot(1, 2, 2)
sns.boxplot(x='gender', y='cholesterol', data=df)
plt.title('Распределение холестерина по полу')

plt.tight_layout()
plt.show()

# 4. Анализ рисков
df['high_bp'] = df['blood_pressure'] > 140
df['high_cholesterol'] = df['cholesterol'] > 240
df['risk_factors'] = df['high_bp'].astype(int) + df['high_cholesterol'].astype(int)

print('\nРаспределение факторов риска:')
print(df['risk_factors'].value_counts().sort_index())

# 5. Корреляционный анализ
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Корреляционная матрица')
plt.show()

# 6. Возрастные группы
df['age_group'] = pd.cut(df['age'], 
                        bins=[0, 30, 45, 60, 100],
                        labels=['<30', '30-45', '45-60', '>60'])

print('\nАнализ заболеваний по возрастным группам:')
print(df.groupby('age_group')['heart_disease'].mean())