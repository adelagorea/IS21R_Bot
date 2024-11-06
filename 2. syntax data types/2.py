def is_even(n):
    """
    Verifică dacă un număr este par.

    :param n: Numărul de verificat
    :return: True dacă este par, False altfel
    """
    return n % 2 == 0

# Testează funcția
print(is_even(4))  # Output: True
print(is_even(7))  # Output: False
