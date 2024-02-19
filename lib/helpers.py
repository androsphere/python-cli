# lib/helpers.py
from models.__init__ import CURSOR
from models.character import Character
from models.item import Item

def list_characters():
    print("Characters: ")
    characters = Character.get_all()
    for character in characters:
        print(character)
    print("Which character would you like to inspect?")
    choice = input("Type 'R' to return to main menu > ")
    e_test(choice)
    if choice.upper() == "R":
        return
    current_character = characters[int(choice)-1]
    print (current_character)
    items = current_character.items()
    for item in items:
        print(item)
    print(f"Total item weight: {current_character.total_item_weight(CURSOR)}" )
    print("What would you like to do with this character?")
    print("1. Edit")
    print("2. Delete")
    print("3: Manage items")
    print("4. Return to main menu")
    edit_or_delete = input ("> ")
    e_test(edit_or_delete)
    if edit_or_delete == "1":
        edit_character(current_character)
    elif edit_or_delete == "2":
        delete_character(current_character)
    elif edit_or_delete == "3":
        edit_character_items(current_character)
    else:
        print("invalid choice")


def edit_character(character):
    
    try:
        name = input("Enter Character's new name: ")
        e_test(name)
        character.name = name
        species = input("Enter the Character's new species: ")
        e_test(species)
        character.species = species
        character_class = input("Enter the character's new class: ")
        e_test(character_class)
        character.character_class = character_class

        character.update()
        print(f'Success: {character}')
    except Exception as exc:
            print("Error updating character: ", exc)

def delete_character(character):
    pass

def edit_character_items(character):
    pass
    
    
    

def add_character():
    name = input("Enter the character's name: >")
    e_test(name)
    species = input("Enter the character's species: >")
    e_test(species)
    character_class = input("Enter ther character's class: >")
    e_test(character_class)
    try:
        character = Character.create(name, species, character_class)
        print(f'Success: {character}')
    except Exception as exc:
        print("Error creating employee: ", exc)

def add_item():
    name = input("Enter the item's name: >")
    e_test(name)
    character = input("Which character will carry it? >")
    e_test(character)
    weight = input("Enter the item's weight in pounds: >")
    e_test(weight)

    character_id = Character.find_by_name(character).id
    try:
        item = Item.create(name, weight, character_id )
        print(f'Success: {item}')
    except Exception as exc:
        print("Error creating item: ", exc)

def e_test(string_input):
    if string_input.upper() == "E":
        exit_program()


def exit_program():
    print("Exiting Program")
    print("Goodbye!")
    exit()
