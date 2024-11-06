def classify_numbers(numbers):
    """
    Clasifică numerele dintr-o listă în pare și impare.

    :param numbers: Lista de numere
    :return: Două liste - una cu numerele pare și alta cu numerele impare
    """
    even_numbers = []
    odd_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    return even_numbers, odd_numbers

# Testează funcția
numbers = [1, 2, 3, 4, 5, 6]
print(classify_numbers(numbers))  # Output: ([2, 4, 6], [1, 3, 5])
