import csv

def read_csv(file_path):
    """
    Citește un fișier CSV și returnează datele sub formă de listă de dicționare.

    :param file_path: Calea către fișierul CSV
    :return: Listă de dicționare cu datele din fișier
    """
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

# Testează funcția
file_path = 'data.csv'
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age'])
    writer.writerow(['Alice', 30])
    writer.writerow(['Bob', 25])

print(read_csv(file_path))  # Output: [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]
