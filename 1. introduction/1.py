def find_max_min(numbers):
    """
    Returnează numerele maxime și minime dintr-o listă.

    :param numbers: Lista de numere
    :return: Tuplu (max, min)
    """
    if not numbers:
        return None
    return (max(numbers), min(numbers))

# Testează funcția
numbers = [3, 5, 1, 9, 4]
print(find_max_min(numbers))  # Output: (9, 1)
