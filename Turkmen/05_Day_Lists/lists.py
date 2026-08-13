# 5-nji Gün - Sanawlar (Lists Practice)

# 1. Sanaw döretmek we Indeks
fruits = ['alma', 'banan', 'oranj', 'nar']
print("Birinji miwe:", fruits[0])
print("Soňky miwe:", fruits[-1])

# 2. Element goşmak we pozmak
fruits.append('erik')
print("Erik goşulandan soň:", fruits)

fruits.remove('banan')
print("Banan pozylyp rejelendi:", fruits)

# 3. Sanawy tertiplemek
numbers = [42, 12, 89, 5, 23]
numbers.sort()
print("Tertiplenen sanlar:", numbers)

# 4. List Slicing
print("Ilki 3 san:", numbers[:3])

# 5. List Unpacking
a, b, *rest = numbers
print("a:", a, "| b:", b, "| Galanlary:", rest)
