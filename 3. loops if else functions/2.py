def sum_up_to(n):
    """
    Calculează suma numerelor de la 1 până la n.

    :param n: Numărul până la care se calculează suma
    :return: Suma numerelor de la 1 până la n
    """
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

# Testează funcția
print(sum_up_to(5))  # Output: 15
