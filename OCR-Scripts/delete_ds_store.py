""" 
Python Delete .DS_Store files
"""

# Import necessary modules
from dotenv import load_dotenv, dotenv_values
import os

"""
Load Environment Variable
"""
load_dotenv()
os_path = os.getenv("WORKING_DIRECTORY")


def delete_ds_store_files(root_folder):
    """Deletes all .DS_Store files within a given root folder and its subfolders.

    Args:
        root_folder: The path to the root folder.
        """

    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith(".DS_Store"):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print("Deleted:", file_path)

# Example usage
root_folder = f"{os_path}/images_source/"
delete_ds_store_files(root_folder)