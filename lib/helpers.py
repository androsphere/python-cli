# lib/helpers.py
from models.character import Character
from models.item import Item

def list_characters():
    characters = Character.get_all()
    for character in characters:
        print(character)

def list_items():
    print("list items")


def exit_program():
    print("Exited Program")
    exit()
