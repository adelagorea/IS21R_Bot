def print_even_numbers(numbers):
    """
    Afișează toate numerele pare dintr-o listă.

    :param numbers: Lista de numere
    """
    for number in numbers:
        if number % 2 == 0:
            print(number)

# Testează funcția
numbers = [1, 2, 3, 4, 5, 6]
print_even_numbers(numbers)  # Output: 2, 4, 6
