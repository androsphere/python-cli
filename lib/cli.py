# lib/cli.py

from helpers import (
    exit_program,
    list_characters,
    add_character,
    add_item
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "E" or choice == "e":
            exit_program()
        elif choice == "1":
            list_characters()

        elif choice == "2":
            add_character()

        elif choice == "3":
            add_item()
        else:
            print("Invalid choice")


def menu():
    print("Welcome to Andy's inventory management program!")
    print("Type E at any time to exit the program")
    print("1: List Characters")
    print("2: Add Character")
    print("3: Add item")



if __name__ == "__main__":
    main()
