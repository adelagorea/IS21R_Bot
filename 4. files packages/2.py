def write_to_file(file_path, content):
    """
    Scrie un șir de caractere într-un fișier.

    :param file_path: Calea către fișierul în care se va scrie
    :param content: Șirul de caractere de scris
    """
    with open(file_path, 'w') as file:
        file.write(content)

# Testează funcția
file_path = 'output.txt'
content = "Aceasta este o scriere de test."
write_to_file(file_path, content)

with open(file_path, 'r') as file:
    print(file.read())  # Output: Aceasta este o scriere de test.
