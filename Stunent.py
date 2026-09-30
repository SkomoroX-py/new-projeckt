import math

def find_lcm(a, b):
    # Якщо обидва числа нулі, НСК дорівнює 0
    if a == 0 and b == 0:
        return 0
    # Формула НСК через НСД (math.gcd)
    return abs(a * b) // math.gcd(a, b)

# Приклад використання:
num1 = 12
num2 = 18
result = find_lcm(num1, num2)

print(f"НСК чисел {num1} та {num2} дорівнює: {result}")
# Виведе: НСК чисел 12 та 18 дорівнює: 36

