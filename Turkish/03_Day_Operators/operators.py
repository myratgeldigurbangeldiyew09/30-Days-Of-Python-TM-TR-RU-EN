# 3. Gün - Operatörler (Derinlemesine Uygulama)

# 1. Aritmetik ve Modulus
num1 = 15
num2 = 4

print(f"Tam Bölme (Floor Division): {num1} // {num2} = {num1 // num2}")
print(f"Mod Bölme (Modulus): {num1} % {num2} = {num1 % num2}")
print(f"Üs Alma: {num1} ** 2 = {num1 ** 2}")

# 2. Kısa Devre Değerlendirmesi (Short-Circuit)
def test_func():
    print("Bu fonksiyon çalıştırıldı!")
    return True

# 'or' işleminde ilk durum True olduğu için test_func çağrılmaz
result = True or test_func()
print("Short-circuit sonucu:", result)

# 3. 'is' ve '==' Farkı
list_a = [1, 2, 3]
list_b = [1, 2, 3]

print("Değerler eşit mi? (list_a == list_b):", list_a == list_b)  # True
print("Bellek adresleri aynı mı? (list_a is list_b):", list_a is list_b)  # False

# 4. Bitwise İşlemler
x = 5  # İkilik: 0101
y = 3  # İkilik: 0011

print(f"Bitwise AND (5 & 3): {x & y}")  # Çıktı: 1 (0001)
print(f"Bitwise OR (5 | 3): {x | y}")   # Çıktı: 7 (0111)

# 5. Pratik Örnekler
# Örnek: Daire Alanı Hesaplama (A = pi * r^2)
PI = 3.14159
radius = 10
area = PI * (radius ** 2)
print(f"Yarıçapı {radius} olan dairenin alanı: {area}")
