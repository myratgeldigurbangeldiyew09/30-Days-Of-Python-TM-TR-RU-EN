# Day 3 - Operators (Advanced Practice)

# 1. Arithmetic & Modulus
num1 = 15
num2 = 4

print(f"Floor Division: {num1} // {num2} = {num1 // num2}")
print(f"Modulus: {num1} % {num2} = {num1 % num2}")
print(f"Exponentiation: {num1} ** 2 = {num1 ** 2}")

# 2. Short-Circuit Evaluation
def test_func():
    print("Function executed!")
    return True

# 'or' condition short-circuits since first operand is True
result = True or test_func()
print("Short-circuit result:", result)

# 3. 'is' vs '==' Comparison
list_a = [1, 2, 3]
list_b = [1, 2, 3]

print("Are values equal? (list_a == list_b):", list_a == list_b)  # True
print("Are RAM addresses identical? (list_a is list_b):", list_a is list_b)  # False

# 4. Bitwise Operations
x = 5  # Binary: 0101
y = 3  # Binary: 0011

print(f"Bitwise AND (5 & 3): {x & y}")  # Output: 1 (0001)
print(f"Bitwise OR (5 | 3): {x | y}")   # Output: 7 (0111)

# 5. Practical Example: Circle Area (A = pi * r^2)
PI = 3.14159
radius = 10
area = PI * (radius ** 2)
print(f"Area of circle with radius {radius}: {area}")
