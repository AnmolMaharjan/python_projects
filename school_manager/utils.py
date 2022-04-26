import os

RECORD_PATH = 'records'


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_message(message: str):
    print(message)