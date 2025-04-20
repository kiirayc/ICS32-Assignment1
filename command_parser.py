# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kira Cho
# kirac4@uci.edu
# 69412294

from notebook import *
from pathlib import *

def create_note(command, notebook):
    '''
    Creates a new notebook file and saves the notebook object to the specified file path.
    Parameters:
        command (list): List containing command arguments.
        notebook (Notebook): The Notebook object to be saved.

    Returns:
        Path: The path of the created notebook file.
    '''

    try:
        new_path = command[1] + "/" + command[3] + ".json"
    
        directory = Path(command[1])
        file_path = Path(new_path)
        
        if directory.exists() and not file_path.exists():

            file = open(file_path, 'w')
            file.close()

            notebook.save(file_path)
            print(f"{file_path} CREATED")

        else:
            print("ERROR")
        
        return file_path
    except:
            print("ERROR")

def delete_note(command):

    '''
    Deletes a notebook file based on the given command.

    Parameters:
        command (list): List containing command arguments.
    '''

    while command:
        if '.json' in command[1]:
            new_path = command[1]        
            file_path = Path(new_path)

            if file_path.exists():
                file_path.unlink()
                print(new_path, 'DELETED')
                break 

            else:
                print("ERROR")

        else:
            print("ERROR")
        
        command = input("")

def load_note(command):
    '''
    Loads a notebook from the specified file if it exists and verifies the username and password.

    Parameters:
        command (list): List containing command arguments.

    Returns:
        Path: The path of the loaded notebook file.
        Notebook: The loaded Notebook object.
    '''

    if '.json' in command[1]:
        file_path = Path(command[1])

        if file_path.exists():
            notebook_name = input("")
            notebook_pw = input("")  

            notebook = Notebook("", "", "")
            notebook.load(command[1])

            if (notebook_name == notebook.username) and (notebook_pw == notebook.password):
                print("Notebook loaded.")
                print(notebook.username)
                print(notebook.bio)
            else:
                print("ERROR")
                    
        return file_path, notebook

def edit_note(command, notebook, path):

    '''
    Edits the properties of a notebook, such as username, password, bio, and diaries.

    Parameters:
        command (list): List containing command arguments.
        notebook (Notebook): The Notebook object to be edited.
        path (Path): The file path of the notebook being edited.
    '''

    success = True
    delete_indices = []

    for idx in range(1, len(command[::]), 2):

        try:
            if idx + 1 >= len(command):
                print("ERROR")
                break

            if "-usr" in command[idx]:    
                notebook.username = command[idx+1]
            
            elif "-pwd" in command[idx]:
                notebook.password = command[idx+1]

            elif "-bio" in command[idx]:
                notebook.bio = command[idx+1]

            elif "-add" in command[idx]:
                diary = Diary(command[idx+1])
                notebook.add_diary(diary)

            elif "-del" in command[idx]:
                delete_indices.append(int(command[idx+1]))

            else:
                print("ERROR")
                break
        
        except:
            print("ERROR")
            break

        notebook.save(path)
                
    for i in sorted(delete_indices, reverse=True):
        success = notebook.del_diary(i)
        if not success:
            print("ERROR")
    notebook.save(path)

def print_note(command, notebook):
    '''
    Prints the details of the notebook, such as username, password, bio, and diary entries, 
    based on the provided command.

    Parameters:
        command (list): List containing command arguments.
        notebook (Notebook): The Notebook object to be printed.
    '''

    for idx in range(1, len(command)):
        try:
            if "-all" in command[idx]:
                print(notebook.username)
                print(notebook.password)
                print(notebook.bio)

                for diary_idx, diary in enumerate(notebook._diaries):
                    print(f"{diary_idx}: {diary['entry']}") #use getentry? 

            elif "-usr" in command[idx]:    
                print(notebook.username)
            
            elif "-pwd" in command[idx]:
                print(notebook.password)

            elif "-bio" in command[idx]:
                print(notebook.bio)

            elif "-diaries" in command[idx]:
                for diary_idx, diary in enumerate(notebook._diaries):
                    print(f"{diary_idx}: {diary['entry']}")

            elif "-diary" in command[idx]:
                diary_idx = int(command[idx+1])
                print(notebook._diaries[diary_idx]['entry'])
                idx += 1 #to skip checking the index

        except: #edge cases: when diary doesn't exist
            print("ERROR")
            break
