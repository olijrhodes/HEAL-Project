from cryptography.fernet import Fernet
import pandas as pd

data = pd.read_csv("MOCK_DATA.csv")

def key_load(key_name):
    with open(key_name, 'rb') as myKey:
        key = myKey.read()
    return key


def file_encrypt(data):
    key = key_load('myKey.key')
    f = Fernet(key)
    try:
        with open(data, 'rb') as file:
            original = file.read()

        encrypted = f.encrypt(original)

        with open(data, 'wb') as file:
            file.write(encrypted)
    except FileNotFoundError:
        print("Sorry File Not Found!")


def file_decrypt(original_file):
    key = key_load('myKey.key')
    f = Fernet(key)

    try:
        with open(original_file, 'rb') as file:
            encrypted = file.read()

        decrypted = f.decrypt(encrypted)

        with open(original_file, 'wb') as file:
            file.write(decrypted)
    except FileNotFoundError:
        print("Sorry File Not Found!")

file_decrypt(data)
file_encrypt(data)