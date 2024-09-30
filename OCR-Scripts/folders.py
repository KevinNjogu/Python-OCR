from dotenv import load_dotenv, dotenv_values
import os


"""
Load Environment Variable
"""
load_dotenv()
os_path = os.getenv("WORKING_DIRECTORY")

def loop_through_folders(parent_folder):
    """
    Loops through all subfolders within a given parent folder.

    Args:
        parent_folder: The path to the parent folder.
    """
    print("\n")
    folders = []

    for root, dirs, files in os.walk(parent_folder):
        for dir in dirs:
            # Do something with each subfolder
            folders.append(dir)
    return folders

# Example usage
parent_folder = f"{os_path}/images_source/NASDAQ/"
output_folders = loop_through_folders(parent_folder)
for folder in output_folders:
    print(folder)