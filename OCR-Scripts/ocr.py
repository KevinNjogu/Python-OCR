""" 
Python Tesseract Script
"""

# Import necessary modules
from PIL import Image
from dotenv import load_dotenv, dotenv_values
import pytesseract
import numpy as np
import os

"""
Load Environment Variable
"""
load_dotenv()
os_path = os.getenv("WORKING_DIRECTORY")

"""
Start of Testing ground of the script
"""

# # Assign variable to name of test image
# filename = 'OCR-Scripts/ImageTest.png'

# # Convert image into an numpy array
# img1 = np.array(Image.open(filename))

# # Use Tesseract to convert the image of numpy array to string
# text = pytesseract.image_to_string(img1)

# # Print the result
# print(text)

"""
End of Testing ground of the script
"""

"""
Steps to read images, perform OCR on them and output to JSON file
"""
### DOW-30 Section

# Get the directory where images are to be sourced from
dow_directory = "OCR-Scripts/images_source/DOW-30/"

# Run a for loop to:
#   1. Get the image name and assign it to a temporary variable
#   2. Convert image into a numpy array
#   3. Perform OCR on the numpy array 
#   4. Save Pytesseract OCR output to a variable
#   4. Save the output variable string into a JSON file

## Loop through all files in the path folder
output_string = ""

for file in os.listdir(path=f"{os_path}/images_source/DOW-30/"):
    # Save the current file name and path
    image_source = f"{os_path}/images_source/DOW-30/{file}"

    # Convert image into an numpy array
    image_np = np.array(Image.open(image_source))

    # Use pytesseract to perform OCR on the numpy array
    text_string = pytesseract.image_to_string(image_np)

    # Save the output into a separate variable to use for writing into JSON file
    output_string += text_string

    # Print worked on files to confirm
    print(f"\nPerformed OCR on '{file}'.")


## Print output of the final variable & data type
print(f"\n{output_string}")
print(output_string.format)