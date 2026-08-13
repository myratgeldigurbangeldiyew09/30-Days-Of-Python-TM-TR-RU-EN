# День 5 - Списки (Lists Practice)

# 1. Создание и индексация
fruits = ['яблоко', 'банан', 'апельсин', 'гранат']
print("Первый фрукт:", fruits[0])
print("Последний фрукт:", fruits[-1])

# 2. Добавление и удаление
fruits.append('абрикос')
print("После добавления абрикоса:", fruits)

fruits.remove('банан')
print("После удаления банана:", fruits)

# 3. Сортировка списка
numbers = [42, 12, 89, 5, 23]
numbers.sort()
print("Отсортированные числа:", numbers)

# 4. Срезы списка
print("Первые 3 числа:", numbers[:3])

# 5. Распаковка списка (Unpacking)
a, b, *rest = numbers
print("a:", a, "| b:", b, "| Остальные:", rest)
