# Import necessary modules
from dotenv import load_dotenv, dotenv_values
import os
import json

"""
Load Environment Variable
"""
load_dotenv()
os_path = os.getenv("WORKING_DIRECTORY")


def read_json_with_newlines(file_path):
    """
    Reads a JSON file containing a single string with newlines and returns a list of strings.

    Args:
        file_path: The path to the JSON file.

    Returns:
        A list of strings separated by newlines.
    """

    with open(file_path, 'r') as f:
        data = json.load(f)

    # Assuming the data is a string
    if isinstance(data, str):
        return data.splitlines()
    else:
        raise ValueError("JSON file must contain a single string.")

# Example usage
file_path = f"{os_path}/output/DOW-30.json"
strings = read_json_with_newlines(file_path)

print(strings)