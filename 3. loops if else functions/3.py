def check_number(n):
    """
    Verifică dacă un număr este pozitiv, negativ sau zero.

    :param n: Numărul de verificat
    :return: Șirul "pozitiv", "negativ" sau "zero"
    """
    if n > 0:
        return "pozitiv"
    elif n < 0:
        return "negativ"
    else:
        return "zero"

# Testează funcția
print(check_number(10))  # Output: pozitiv
print(check_number(-5))  # Output: negativ
print(check_number(0))  # Output: zero
