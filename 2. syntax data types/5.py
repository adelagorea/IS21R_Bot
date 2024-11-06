def count_frequencies(lst):
    """
    Calculează frecvența fiecărui element dintr-o listă.

    :param lst: Lista de elemente
    :return: Dicționar cu frecvențele elementelor
    """
    frequencies = {}
    for item in lst:
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1
    return frequencies

# Testează funcția
elements = ['a', 'b', 'a', 'c', 'b', 'a']
print(count_frequencies(elements))  # Output: {'a': 3, 'b': 2, 'c': 1}
