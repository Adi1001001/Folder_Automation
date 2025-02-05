import os
import subprocess

def create_project(folder_name, files, old_project_path):
    vscode_path = "C:\\Users\\Adi\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
    file_paths = []
    licence = "MIT License \n\nCopyright (c) [Year] [Full Name] \n\nPermission is hereby granted, free of charge, to any person obtaining a copy \nof this software and associated documentation files (the 'Software'), to deal \nin the Software without restriction, including without limitation the rights \nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell \ncopies of the Software, and to permit persons to whom the Software is \nfurnished to do so, subject to the following conditions: \n\nThe above copyright notice and this permission notice shall be included in all \ncopies or substantial portions of the Software. \n\nTHE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR \nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, \nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE \nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER \nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, \nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE \nSOFTWARE."
    """Creates a folder and specified files, then opens it in VS Code."""
    
    # Get the current working directory and create the project path
    project_path = os.path.join(old_project_path, folder_name)
    
    try:
        # Create the folder
        os.makedirs(project_path, exist_ok=True)

        # Create files inside the folder
        for file in files:
            file_path = os.path.join(project_path, file)
            if not os.path.exists(file_path):
                if file == 'LICENCE':
                    with open(file_path, "w") as f:
                        f.write(licence)  # Add the licence
            file_paths.append(file_path)

        database_handling_ask = input("Do you want a database_handling.py file with sqlite3? ").strip().lower()
        if database_handling_ask == 'y' or database_handling_ask == "yes":
            file_path = os.path.join(project_path, "database_handling.py")
            with open(file_path, "w") as f:
                f.write("import sqlite3")  # Add sqlite3
            with open(f"{project_path}\\requirements.txt", "w") as f:
                f.write("sqlite3")  # Add sqlite3
            file_paths.append(file_path)
        
        assets_ask = input("Do you want an Assets folder? ").strip().lower()
        if assets_ask == 'y' or assets_ask == "yes":
            # Create the assets folder inside the project
            folder_path = os.path.join(project_path, "Assets")
            os.makedirs(folder_path, exist_ok=True)

        log_ask = input("Do you want a log.txt file? ").strip().lower()
        if log_ask == 'y' or log_ask == "yes":
            file_path = os.path.join(project_path, "log.txt")
            file_paths.append(file_path)

        # Open the project folder in VS Code
        subprocess.run([vscode_path, "--new-window", project_path, *file_paths], check=True)

    except Exception as e:
        pass

def set_project_name():
    return input('What will your projects name be? ')