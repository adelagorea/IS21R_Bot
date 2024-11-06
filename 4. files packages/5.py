import pandas as pd

def read_excel(file_path, sheet_name):
    """
    Citește un fișier Excel și returnează datele dintr-o foaie specificată.

    :param file_path: Calea către fișierul Excel
    :param sheet_name: Numele foii de citit
    :return: DataFrame cu datele din foaie
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df

# Testează funcția
file_path = 'data.xlsx'
data = {
    'name': ['Alice', 'Bob'],
    'age': [30, 25]
}
df = pd.DataFrame(data)
df.to_excel(file_path, sheet_name='Sheet1', index=False)

print(read_excel(file_path, 'Sheet1'))
# Output:
#     name  age
# 0  Alice   30
# 1    Bob   25
