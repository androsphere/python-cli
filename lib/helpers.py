# lib/helpers.py
from models.character import Character
from models.item import Item

def list_characters():
     # choice = input("Please select a character")
    characters = Character.get_all()
    for character in characters:
        print(character)
    
    

def list_items():
    print("list items")

def add_character():
    name = input("Enter the character's name: ")
    species = input("Enter the character's species: ")
    character_class = input("Enter ther character's class: ")
    try:
        character = Character.create(name, species, character_class)
        print(f'Success: {character}')
    except Exception as exc:
        print("Error creating employee: ", exc)

def add_item():
    name = input("Enter the item's name: ")
    character = input("Which character does this item belong to? ")
    weight = input("Enter the item's weight")

    character_id = Character.find_by_name(character).id
    try:
        item = Item.create(name, character_id , weight)
        print(f'Success: {item}')
    except Exception as exc:
        print("Error creating item: ", exc)


def exit_program():
    print("Exited Program")
    exit()
