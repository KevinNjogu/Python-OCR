""" 
Python Tesseract Script
"""

# Import necessary modules
from PIL import Image
import pytesseract
import numpy as np

"""
Start of the script
"""

# Assign variable to name of test image
filename = 'images_source/DOW-30/DOW 30_page-0001.jpg'
# Convert image into an numpy array
img1 = np.array(Image.open(filename))
# Use Tesseract to convert the image of numpy array to text
text = pytesseract.image_to_string(img1)
# Print the result
print(text)