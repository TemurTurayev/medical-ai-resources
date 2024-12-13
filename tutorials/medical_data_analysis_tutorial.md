# Анализ медицинских данных с помощью Python и Pandas

## Подготовка окружения

Сначала нам нужно установить необходимые библиотеки. В Anaconda они уже предустановлены, но если нет:

```bash
pip install pandas matplotlib seaborn
```

## Пошаговый анализ данных

### 1. Импорт библиотек и создание данных

```python
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
```

### 2. Базовый анализ данных

```python
# Просмотр первых строк данных
print("Первые 5 записей:")
print(df.head())

# Основная статистика
print("\nСтатистика по данным:")
print(df.describe())

# Информация о данных
print("\nИнформация о данных:")
print(df.info())
```

### 3. Анализ распределений

```python
# Распределение по полу
gender_dist = df['gender'].value_counts()
print("\nРаспределение по полу:")
print(gender_dist)

# Средние значения по полу
print("\nСредние значения по полу:")
print(df.groupby('gender').mean())
```

### 4. Визуализация данных

```python
# Создаём график
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
```

### 5. Анализ рисков

```python
# Определяем факторы риска
df['high_bp'] = df['blood_pressure'] > 140  # Высокое давление
df['high_cholesterol'] = df['cholesterol'] > 240  # Высокий холестерин

# Подсчёт факторов риска
df['risk_factors'] = df['high_bp'].astype(int) + df['high_cholesterol'].astype(int)

print('Распределение факторов риска:')
print(df['risk_factors'].value_counts().sort_index())
```

## Практические задания

1. Попробуйте добавить новые данные:
   - Вес пациента
   - Уровень сахара в крови
   - История курения

2. Создайте новые визуализации:
   - Гистограмма возраста
   - График корреляции между всеми числовыми параметрами
   - Тепловая карта корреляций

3. Рассчитайте дополнительные статистики:
   - Процент пациентов с высоким риском
   - Средний возраст пациентов с заболеванием
   - Распределение факторов риска по возрастным группам

## Полезные функции Pandas для анализа

- `df.corr()` - матрица корреляций
- `df.groupby()` - группировка данных
- `df.value_counts()` - подсчёт уникальных значений
- `df.describe()` - базовая статистика
- `df.isnull().sum()` - проверка пропущенных значений

## Дополнительные методы анализа

### Корреляционный анализ
```python
# Создаём тепловую карту корреляций
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Корреляционная матрица')
plt.show()
```

### Возрастные группы
```python
# Создаём возрастные группы
df['age_group'] = pd.cut(df['age'], 
                        bins=[0, 30, 45, 60, 100],
                        labels=['<30', '30-45', '45-60', '>60'])

# Анализ по возрастным группам
print(df.groupby('age_group')['heart_disease'].mean())
```

### Статистические тесты
```python
from scipy import stats

# T-test для сравнения давления между группами с заболеванием и без
healthy = df[df['heart_disease'] == 0]['blood_pressure']
sick = df[df['heart_disease'] == 1]['blood_pressure']
t_stat, p_value = stats.ttest_ind(healthy, sick)
print(f'P-value for blood pressure difference: {p_value}')
```
