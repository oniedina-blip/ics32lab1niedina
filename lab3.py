# NAME: Oleksandra Niedina
# EMAIL: oniedina@uci.edu
# STUDENT ID: 37948370

from pathlib import Path

File_Name = "pynote.txt"

def get_file_path():
    return Path(File_Name)


def display_notes(file_path):
    print("Welcome to PyNote!")
    print("Here are your notes:\n")

    if file_path.exists():
        with open(file_path, "r") as file:
            notes = file.readlines()
            for note in notes:
                print(note.strip())
                print()  
    else:
        file_path.touch() 


def add_notes(file_path):
    while True:
        user_input = input("Please enter a new note (enter q to exit): ")

        if user_input == "q":
            break

        with open(file_path, "a") as file:
            file.write(user_input + "\n")


def main():
    file_path = get_file_path()
    display_notes(file_path)
    add_notes(file_path)


if __name__ == "__main__":
    main()
