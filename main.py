from util import *
from database_handling import *

# Define the folder name and files
files = ["main.py", "README.md", "requirements.txt", ".gitignore", "util.py", "LICENCE"]

# Run the function
path = check_folder_path()
if path == None:
    desired_folder_path = input('What do you want your folder path to be? ')
    folder_path(desired_folder_path)
else:
    changing = input('Do you want to change your folder path (y/n)').strip().lower()
    if changing == 'y' or changing == 'yes':
        desired_folder_path = input('What do you want your folder path to be? ')
        folder_path(desired_folder_path)

current_folder_path = check_folder_path()
folder_name = set_project_name()
create_project(folder_name, files, current_folder_path)