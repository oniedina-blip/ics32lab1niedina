"""
This program enables a user to input short one line notes and have them stored in a file called pynote.txt
"""

from pathlib import Path
import os

NOTES_PATH = "."
NOTES_FILE = "pynote.txt"

def is_int(val):
    try:
        int(val)
        return True
    except (ValueError, TypeError):
        return False


def save_note(note: str):
    p = Path(NOTES_PATH) / NOTES_FILE
    if not p.exists():
        p.touch(exist_ok=True)
    f = p.open('a')
    f.write(note + '\n')
    f.close()


def read_notes():
    p = Path(NOTES_PATH) / NOTES_FILE
    if not p.exists():
        return
    print("Here are your notes: \n")
    f = p.open()

    for line in f:
        print(line)
    f.close()


def remove_note() -> str:
    p = Path(NOTES_PATH) / NOTES_FILE

    if not p.exists():
        """
        REQUIREMENT 3 - Should be very similar, custom message not required.
        - remove the <bla line> and uncomment the <bla2 line> to complete 3.
        """
        # return                        <bla line>
        raise FileNotFoundError       # <bla2 line>

    print("Here are your notes: \n")

    f = p.open()
    id = 1
    lines = []
    for line in f:
        lines.append(line)
        print(f"{id}: {line}")
        id = id + 1
    f.close()

    remove_id = input("Enter the number of the note you would like to remove: ")
    if not is_int(remove_id):
        print("Not a valid number, cancelling operation.")
        return ""

    f = p.open('w')
    id = 1
    removed_note = ""
    for line in lines:

        if id == int(remove_id):
            removed_note = line
        else:
            f.write(line)
        id = id + 1
    f.close()
    return removed_note


# REQ-1 
assert is_int(5) == True
assert is_int("10") == True
assert is_int("abc") == False
assert is_int(None) == False
assert is_int(1.5) == False


# REQ-2 
if os.path.exists(NOTES_FILE):
    os.remove(NOTES_FILE)

try:
    remove_note()
    assert False, "AssertionError: FileNotFoundError was not raised"
except FileNotFoundError:
    pass


def run():
    try:
        note = input("Please enter a note (enter :d to delete a note or :q to exit):  ")
        if note == ":d":
            try:

                note = remove_note()
                print(f"The following note has been removed: \n\n {note}")
            except FileNotFoundError:
                print("No notes file found to delete from.")
        elif note == ":q":
            return
        else:
            save_note(note)
        run()
    except EOFError:
        return


if __name__ == "__main__":
    print("Welcome to PyNote! \n")
    read_notes()
    run()
