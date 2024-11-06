def factorial(n):
    """
    Returnează factorialul unui număr.

    :param n: Întreg
    :return: Factorialul lui n
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Testează funcția
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
