# 5. Gün - Listeler (Lists Practice)

# 1. Liste Oluşturma ve İndeksleme
fruits = ['elma', 'muz', 'portakal', 'nar']
print("İlk meyve:", fruits[0])
print("Son meyve:", fruits[-1])

# 2. Eleman Ekleme ve Silme
fruits.append('kayısı')
print("Kayısı eklendikten sonra:", fruits)

fruits.remove('muz')
print("Muz silindikten sonra:", fruits)

# 3. Listeyi Sıralama
numbers = [42, 12, 89, 5, 23]
numbers.sort()
print("Sıralanmış sayılar:", numbers)

# 4. List Slicing
print("İlk 3 sayı:", numbers[:3])

# 5. List Unpacking
a, b, *rest = numbers
print("a:", a, "| b:", b, "| Kalanlar:", rest)
