# День 2 - Переменные и встроенные функции

# Объявление переменных
first_name = 'Myrat'
last_name = 'Gurbangeldiýew'
country = 'Turkmenistan'
age = 17
is_married = False
skills = ['Python', 'C++', 'C#']

# Объявление нескольких переменных в одну строку
name, year, is_student = 'Myrat', 2026, True

# Использование встроенных функций
print('Имя:', first_name)
print('Длина имени:', len(first_name))
print('Навыки:', skills)

# Преобразование типов (Type casting)
num_str = '10'
num_int = int(num_str)
print('Преобразование:', type(num_str), '->', type(num_int))

# Округление Float до Int
gravity = 9.81
print('Целое число:', int(gravity))  # Вывод: 9
