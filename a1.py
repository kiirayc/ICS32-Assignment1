# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kira Cho
# kirac4@uci.edu
# 69412294

from notebook import *
from command_parser import *
import shlex

def main():
    '''
    Main function that handles user input and executes commands for managing notebooks. 
    '''
    note = None #check the condition
    note_path = ""
    user_command = shlex.split(input(""))

    while user_command[0] != "Q":
        if len(user_command) <= 1:
            print("ERROR")
            user_command = shlex.split(input(""))
            continue

        if user_command[0] == "C":
            name = input("")
            pw = input("")
            bio = input("")

            note = Notebook(name, pw, bio)

            note_path = create_note(user_command, note) 
        
        elif user_command[0] == "D":
            delete_note(user_command)

        elif user_command[0] == "O":
            try:
                note_path, note = load_note(user_command)
            except:
                print("ERROR")
            
        elif user_command[0] == "E":
            if note == None: #a condition for when C or O commands are not issued 
                print("ERROR")
            else:
                edit_note(user_command, note, note_path)

        elif user_command[0] == "P":
            if note == None: #a condition for when C or O commands are not issued 
                print("ERROR")
            else:
                print_note(user_command, note)
        
        else:
            print("ERROR")

        user_command = input("")
        user_command = shlex.split(user_command)

if __name__ == "__main__":
    main()
