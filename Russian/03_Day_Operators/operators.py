# День 3 - Операторы (Глубокая практика)

# 1. Арифметика и остаток
num1 = 15
num2 = 4

print(f"Целочисленное деление: {num1} // {num2} = {num1 // num2}")
print(f"Остаток от деления: {num1} % {num2} = {num1 % num2}")
print(f"Возведение в степень: {num1} ** 2 = {num1 ** 2}")

# 2. Ленивые вычисления (Short-Circuit)
def test_func():
    print("Функция была вызвана!")
    return True

# В 'or' первое условие True, поэтому test_func() не вызывается
result = True or test_func()
print("Результат short-circuit:", result)

# 3. Разница между 'is' и '=='
list_a = [1, 2, 3]
list_b = [1, 2, 3]

print("Значения равны? (list_a == list_b):", list_a == list_b)  # True
print("Один и тот же объект в памяти? (list_a is list_b):", list_a is list_b)  # False

# 4. Побитовые операции
x = 5  # Двоичное: 0101
y = 3  # Двоичное: 0011

print(f"Побитовое AND (5 & 3): {x & y}")  # Вывод: 1 (0001)
print(f"Побитовое OR (5 | 3): {x | y}")   # Вывод: 7 (0111)

# 5. Практический пример: Площадь круга (A = pi * r^2)
PI = 3.14159
radius = 10
area = PI * (radius ** 2)
print(f"Площадь круга с радиусом {radius}: {area}")
