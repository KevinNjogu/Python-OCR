from dotenv import load_dotenv, dotenv_values
import os
import json

"""
    Load Environment Variable
"""
load_dotenv()
os_path = os.getenv("WORKING_DIRECTORY")


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

# Example usage
my_array = [1, 2, 3, 2, 4, 1, 5]
unique_array = remove_duplicates(my_array)
print(unique_array)  # Output: [1, 2, 3, 4, 5]