# lib/cli.py

from helpers import (
    exit_program,
    list_characters,
    list_items
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
            list_items()
        else:
            print("Invalid choice")


def menu():
    print("Welcome to Andy's inventory management program!")
    print("Please select an option:")
    print("E. Exit the program")
    print("1. List Current Characters")



if __name__ == "__main__":
    main()
