# lib/helpers.py
from models.__init__ import CURSOR
from models.character import Character
from models.item import Item

def list_characters():
    characters = Character.get_all()
    if len(characters) == 0:
        print("No characters in database")
        return
    print("")
    print("Characters: ")
    for index, character in  enumerate(characters, start=1):
        print(f"{index}. {character.name}: {character.species} {character.character_class}")
    print("Which character would you like to inspect?")
    choice = input("Type 'R' to return to main menu > ")
    e_test(choice)
    if choice.upper() == "R":
        return
    if choice.isnumeric() == False or int(choice) >= len(characters) + 1:
        print("Invalid choice")
        return
    current_character = characters[int(choice)-1]
    print("")
    print (f"{current_character.name} selected.")
    items = current_character.items()
    for item in items:
        print(f"{item.name}, {item.weight} pounds")
    print(f"Total inventory weight: {current_character.total_item_weight(CURSOR)} pounds." )
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
        current_character.delete()
        print("Character deleted")
    elif edit_or_delete == "3":
        list_character_items(current_character)
    elif edit_or_delete == "4":
        return
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


def list_character_items(character):
    items = character.items()
    for index, item in  enumerate(items, start=1):
        print(f"{index}. {item.name}, {item.weight} pounds ")
    print("Type 'R' to return to main menu")
    choice = input("Which Item would you like to inpect? > ")
    if choice.upper() == "R":
        return
    if choice >= len(items):
        print("Invalid choice")
    e_test(choice)
    current_item = items[int(choice)-1]
    print(f"{current_item.name} Selected")
    print("1. Edit item")
    print("2. Delete item")
    edit_or_delete = input("> ")
    e_test(edit_or_delete)
    if edit_or_delete == "1":
        edit_item(current_item)
    elif edit_or_delete == "2":
        current_item.delete()
        print("Item deleted ")
        print("")
    else:
        print("Invalid input ")

def edit_item(item):
    try:
        name = input("Enter the item's new name: >")
        e_test(name)
        item.name = name
        weight = input("Enter the item's new weight in pounds: >")
        e_test(weight)
        item.weight = int(weight)
        character = input("Which character will carry it? > ")
        e_test(character)
        character_id = Character.find_by_name(character).id
        item.character_id = character_id
        item.update()
        print(f'Success: {item}')
    except Exception as exc:
        print("Error updating item: ", exc)


def add_character():
    name = input("Enter the character's name: >")
    e_test(name)
    species = input("Enter the character's species: >")
    e_test(species)
    character_class = input("Enter ther character's class: >")
    e_test(character_class)
    try:
        character = Character.create(name, species, character_class)
        print(f'Success: {character.name} has joined the game!')
    except Exception as exc:
        print("Error creating employee: ", exc)

def add_item():
    name = input("Enter the item's name: >")
    e_test(name)
    character_input= input("Which character will carry it? >")
    e_test(character_input)
    weight = input("Enter the item's weight in pounds: >")
    e_test(weight)
    characters = [character.name for character in Character.get_all()]
    if character_input in characters:
        pass
    else:
        print("Item can only be added to existing character")
        return
    character_id = Character.find_by_name(character_input).id
    try:
        item = Item.create(name, int(weight), character_id )
        print(f'Success:{character_input} now has {item.name}')
    except Exception as exc:
        print("Error creating item: ", exc)


def e_test(string_input):
    if string_input.upper() == "E":
        print("Exiting Program")
        print("Goodbye!")
        exit()



