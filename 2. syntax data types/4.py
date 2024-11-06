def classify_number(n):
    """
    Clasifică un număr ca fiind pozitiv, negativ sau zero.

    :param n: Numărul de clasificat
    :return: "pozitiv", "negativ" sau "zero"
    """
    if n > 0:
        return "pozitiv"
    elif n < 0:
        return "negativ"
    else:
        return "zero"

# Testează funcția
print(classify_number(10))  # Output: pozitiv
print(classify_number(-5))  # Output: negativ
print(classify_number(0))  # Output: zero
