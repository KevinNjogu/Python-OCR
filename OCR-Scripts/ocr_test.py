""" 
Python Tesseract Test/Demo Script
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
Start of Testing ground of the script
"""

# Assign variable to name of test image
filename = 'ImageTest.png'

# Convert image into an numpy array
img1 = np.array(Image.open(filename))

# Use Tesseract to convert the image of numpy array to string
text = pytesseract.image_to_string(img1)

# Print the result
print(text)

"""
End of Testing ground of the script
"""