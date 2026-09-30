import math

def find_hypotenuse(a, b):
    """
    Calculates the hypotenuse of a right-angled triangle given the two legs.
    """
    return math.hypot(a, b)

# Приклад використання:
katet1 = 3
katet2 = 4
gipotenuza = find_hypotenuse(katet1, katet2)

print(f"Гіпотенуза трикутника з катетами {katet1} та {katet2} дорівнює: {gipotenuza}")
