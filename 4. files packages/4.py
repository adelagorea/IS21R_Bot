import json

def write_to_json(file_path, data):
    """
    Scrie un dicționar într-un fișier JSON.

    :param file_path: Calea către fișierul JSON
    :param data: Dicționarul de scris în fișier
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Testează funcția
file_path = 'data.json'
data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
write_to_json(file_path, data)

with open(file_path, 'r') as file:
    print(file.read())  # Output: {"name": "Alice", "age": 30, "city": "New York"}
