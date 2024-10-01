""" 
Python Tesseract Script
"""

# Import necessary modules
from PIL import Image
from dotenv import load_dotenv, dotenv_values
import pytesseract
import numpy as np
import os
import json

"""
Load Environment Variable
"""
load_dotenv()
os_path = os.getenv("WORKING_DIRECTORY")


"""
OCR Function
"""

def perform_ocr_on(input_path, output_path, output_filename):
    """
    How to feed in the variables:
        1. input_path: write the path where the individual images are stored
                        starting from where the folder after where script is running
                        up to the image(s) location
        2. output_path: write the path to where the output should be saved to. It's best
                        if the folder already exists so that it's saved inside.
        3. output_filename: the name of the output file containing the string(s). The
                        function will add the JSON extension for you.

    Function purpose:
        1. Loading the image(s) in a folder to perform OCR on
        2. Perform OCR on the image(s)
        3. Save output to a temporary variable
        4. Write the output as string to a JSON file
        5. Return the list of images processed in your terminal
    """ 

    ## Create temp variables
    # Path of folder containing images to perform OCR on starting from script's path
    input_folder_path = input_path

    # String output variable after performing OCR
    output_string = ""

    # Path of folder to output to 
    output_folder_path = output_path

    # Name of output JSON file
    output_json_name = output_filename

    # Loop for performing OCR on images in the folder
    for file in os.listdir(path=f"{os_path}{input_folder_path}"):
        # Save the current file name and path
        image_source = f"{os_path}{input_folder_path}{file}"

        # Convert image into an numpy array
        image_np = np.array(Image.open(image_source))

        # Use pytesseract to perform OCR on the numpy array
        text_string = pytesseract.image_to_string(image_np)

        # Save the output into a separate variable to use for writing into JSON file
        output_string += text_string

    ## Writing to JSON file
    with open(f"{os_path}{output_folder_path}{output_json_name}.json", "w") as final:
        json.dump(output_string, final)

    # Print worked on files to confirm
    print("\nPerformed OCR on:\n")
    for file in os.listdir(path=f"{os_path}{input_folder_path}"):
        print(f"{file}\n")



# DOW OCR Processing
# dow_input_directory = "/images_source/DOW-30/"
# dow_output_directory = "/output/"
# dow_file_name = "DOW-30"
# perform_ocr_on(dow_input_directory, dow_output_directory, dow_file_name)

# # S&P OCR Processing
# s_and_p_input_directory = "/images_source/Flaire-—-S&P-500-Companies:-Full-List-and-Performance---NerdWallet/"
# s_and_p_output_directory = "/output/"
# s_and_p_file_name = "S&P-500"
# perform_ocr_on(s_and_p_input_directory, s_and_p_output_directory, s_and_p_file_name)


"""
Folder Loop Function
"""

def loop_through_folders(parent_folder):
    """
    Loops through all subfolders within a given parent folder.

    Args:
        parent_folder: The path to the parent folder.
    """
    folders = []

    for root, dirs, files in os.walk(parent_folder):
        for dir in dirs:
            # Append the full path to root folder containing images
            folders.append(dir)
    return folders

### NASDAQ Folder Loop & OCR Function Section Start
## Folder Loop Function Section
nasdaq_parent_folder = f"{os_path}/images_source/NASDAQ"
nasdaq_output_folders = loop_through_folders(nasdaq_parent_folder)
nasdaq_final_path = []
nasdaq_root_path = "/images_source/NASDAQ/"
for folder in nasdaq_output_folders:
    nasdaq_final_path.append(nasdaq_root_path+folder)

## OCR Function Section
nasdaq_input_directories = nasdaq_final_path
nasdaq_output_directory = "/output/"
nasdaq_file_name = "NASDAQ"
for folder in nasdaq_input_directories:
    perform_ocr_on(folder, nasdaq_output_directory, nasdaq_file_name)
    print(f"Worked on {folder}")

## NASDAQ Folder Loop & OCR Function Section End

### NYSE Folder Loop & OCR Function Section Start
## Folder Loop Function Section
# nyse_parent_folder = f"{os_path}/images_source/NYSE"
# nyse_output_folders = loop_through_folders(nyse_parent_folder)

# ## OCR Function Section
# final_path = []
# root_path = "/images_source/NYSE/"
# nyse_output_directory = "/output/"
# nyse_file_name = "NASDAQ"
# for folder in nyse_output_folders:
#     final_path.append(root_path+folder)
# for path in final_path:
#     print(path)

### NYSE Folder Loop & OCR Function Section End



