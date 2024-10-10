# Import necessary modules
from dotenv import load_dotenv, dotenv_values
import os
import json

"""
    Load Environment Variable
"""
load_dotenv()
os_path = os.getenv("WORKING_DIRECTORY")

"""
    Function for reading single line string and returning array of strings
"""
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

"""
    Function for deleting duplicates in Array
"""
def remove_duplicates(arr):
    """
        Removes duplicate elements from an array.
        
        Args:
            arr: The array to remove duplicates from.

        Returns:
            A new array without duplicates.
    """

    seen = set()
    result = []
    for element in arr:
        if element not in seen:
            seen.add(element)
            result.append(element)
    return result


"""
    Remove Empty Strings,
    Delete Duplicate Entries &
    Write Output to refined_output Folder Section
"""
## Start of DOW Processing
dow_file_path = f"{os_path}/output/DOW-30.json"
dow_strings = read_json_with_newlines(dow_file_path)
dow_list = list(filter(None, dow_strings))
dow_final = remove_duplicates(dow_list)

## Writing to DOW JSON file
with open(f"{os_path}/refined_output/DOW-30.json", "w") as final:
    json.dump(dow_final, final)

## End of DOW Processing


## Start of S&P Processing
s_and_p_file_path = f"{os_path}/output/S&P-500.json"
s_and_p_strings = read_json_with_newlines(s_and_p_file_path)
s_and_p_list = list(filter(None, s_and_p_strings))
s_and_p_final = remove_duplicates(s_and_p_list)

## Writing to S&P JSON file
with open(f"{os_path}/refined_output/S&P-500.json", "w") as final:
    json.dump(s_and_p_final, final)

## End of S&P Processing

## Start of NASDAQ Processing
nasdaq_file_path = f"{os_path}/output/NASDAQ.json"
nasdaq_strings = read_json_with_newlines(nasdaq_file_path)
nasdaq_list = list(filter(None, nasdaq_strings))
nasdaq_final = remove_duplicates(nasdaq_list)

## Writing to DOW JSON file
with open(f"{os_path}/refined_output/NASDAQ.json", "w") as final:
    json.dump(nasdaq_final, final)

## End of NASDAQ Processing

## Start of NYSE Processing
nyse_file_path = f"{os_path}/output/NYSE.json"
nyse_strings = read_json_with_newlines(nyse_file_path)
nyse_list = list(filter(None, nyse_strings))
nyse_final = remove_duplicates(nyse_list)

## Writing to NYSE JSON file
with open(f"{os_path}/refined_output/NYSE.json", "w") as final:
    json.dump(nyse_final, final)

## End of NYSE Processing
