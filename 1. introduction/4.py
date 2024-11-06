def divide(a, b):
    """
    Împarte două numere și gestionează împărțirea la zero.

    :param a: Numărător
    :param b: Numitor
    :return: Rezultatul împărțirii sau mesaj de eroare
    """
    try:
        result = a / b
    except ZeroDivisionError:
        return "Eroare: Împărțirea la zero nu este permisă."
    return result

# Testează funcția
print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: Eroare: Împărțirea la zero nu este permisă.
