# 3-nji Gün - Operatorlar (Çuňňur amalyýet)

# 1. Arifmetika we Modulus
num1 = 15
num2 = 4

print(f"Bütin bölmek (Floor Division): {num1} // {num2} = {num1 // num2}")
print(f"Qalgyly bölmek (Modulus): {num1} % {num2} = {num1 % num2}")
print(f"Dereje galdyrmak: {num1} ** 2 = {num1 ** 2}")

# 2. Short-Circuit Evaluation (Tizleşdirilen Barlag)
def test_func():
    print("Bu funksiýa çagyryldy!")
    return True

# 'or' amalynda ilkinji True tapan badyna test_func çagyrylmaýar
result = True or test_func()
print("Short-circuit result:", result)

# 3. 'is' we '==' Tapawudyny Barlamak
list_a = [1, 2, 3]
list_b = [1, 2, 3]

print("Bahalar deňmi? (list_a == list_b):", list_a == list_b)  # True
print("Ýatdaky salgylary deňmi? (list_a is list_b):", list_a is list_b)  # False (aýry RAM salgylary)

# 4. Bitwise Amallar (Bit tizlikleri)
x = 5  # Ikilik kody: 0101
y = 3  # Ikilik kody: 0011

print(f"Bitwise AND (5 & 3): {x & y}")  # Output: 1 (0001)
print(f"Bitwise OR (5 | 3): {x | y}")   # Output: 7 (0111)

# 5. Amaly Gönükmeler (Exercises)
# Gönükme 1: Geometrik formulany hasaplamak (Daireniň meýdany: A = pi * r^2)
PI = 3.14159
radius = 10
area = PI * (radius ** 2)
print(f"Radiusy {radius} bolan daireniň meýdany: {area}")
