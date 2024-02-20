# lib/cli.py

from helpers import (
    list_characters,
    add_character,
    add_item,
    e_test
)


def main():
    while True:
        menu()
        choice = input("> ")
        e_test(choice)
        if choice == "1":
            list_characters()

        elif choice == "2":
            add_character()

        elif choice == "3":
            add_item()
        else:
            print("Invalid choice")


def menu():
    print("")
    print("Welcome to Andy's inventory management program!")
    print("Type E at any time to exit the program")
    print("1: List Characters")
    print("2: Add Character")
    print("3: Add item")



if __name__ == "__main__":
    main()
