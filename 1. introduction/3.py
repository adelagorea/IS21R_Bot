def copy_file(source_file, target_file):
    """
    Copiază conținutul din source_file în target_file.

    :param source_file: Calea către fișierul sursă
    :param target_file: Calea către fișierul țintă
    """
    with open(source_file, 'r') as src, open(target_file, 'w') as tgt:
        for line in src:
            tgt.write(line)

# Testează funcția
source_file = 'source.txt'
target_file = 'target.txt'
with open(source_file, 'w') as f:
    f.write("Hello, World!\nThis is a test.")

copy_file(source_file, target_file)

with open(target_file, 'r') as f:
    print(f.read())  # Output: Hello, World!\nThis is a test.
