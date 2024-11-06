import configparser

def read_config(file_path):
    """
    Citește un fișier de configurație ini și returnează datele sub formă de dicționar.

    :param file_path: Calea către fișierul ini
    :return: Dicționar cu datele din fișierul de configurație
    """
    config = configparser.ConfigParser()
    config.read(file_path)
    config_dict = {section: dict(config.items(section)) for section in config.sections()}
    return config_dict

def write_config(file_path, config_dict):
    """
    Scrie un dicționar într-un fișier de configurație ini.

    :param file_path: Calea către fișierul ini
    :param config_dict: Dicționarul de scris în fișier
    """
    config = configparser.ConfigParser()
    for section, options in config_dict.items():
        config[section] = options
    with open(file_path, 'w') as configfile:
        config.write(configfile)

# Testează funcțiile
file_path = 'config.ini'
config_data = {
    'Settings': {
        'theme': 'dark',
        'version': '1.0.0'
    },
    'User': {
        'name': 'Alice',
        'email': 'alice@example.com'
    }
}
write_config(file_path, config_data)
print(read_config(file_path))
# Output: {'Settings': {'theme': 'dark', 'version': '1.0.0'}, 'User': {'name': 'Alice', 'email': 'alice@example.com'}}
