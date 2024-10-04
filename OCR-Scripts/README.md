# OCR Using Tesseract
### Fun Fact: The Tesseract OCR was made by the Google team & coincidentally, the Tesseract is the same cube shaped stone featured in the Marvel Cinematic universe popularized by Lokki.

## How to Install, Configure & Run this script
1. Open the CMD(Terminal) on your machine at the root of the project foler
2. Make sure you have Python installed (Python > 3.9)
3. Create a virtual environment by running `python3 -m venv venv`
    - This will create a virtual environment named **venv**
4. Run `source venv/bin/activate` on *Unix* OR `venv\Scripts\activate` on *Windows* to activate the environment.
    - Your terminal/cmd should have **(venv)** at the very start
5. Then run `pip install -r virtual_environment.txt` to install the dependencies.
    - The `-r` flag is to make the command persist installing the dependencies incase they are not immediately visible on 1sr try.
6. Next, if you **do not have Tesseract installed as a stand-alone package**, follow the instructions in **How to Build Optical Character Recognition (OCR) in Python** the resource below to install for your OS.
7. Once done, navigate to `OCR-Scripts/` then run `python ocr_test.py` to execute the file from the command line. 
    - Run line 7 incase running the file directly from your editor causes issues.

## Security Configurations
1. Create a **.env** file at the root of the project.
2. Open the **.env** file and insert the absolute path up to the root of the project folder as shown in the example below:
    - `WORKING_DIRECTORY = "/USER/PATH/PATH/.../FOLDER HOLDING THE PROJECT/OCR-Scripts"`
    - Where the `/PATH/` & `/FOLDER HOLDING THE PROJECT/` are folders before getting to the project folder

### Resources
1. [How to Build Optical Character Recognition (OCR) in Python](https://builtin.com/data-science/python-ocr)
2. [Convert Python List to Json](https://www.geeksforgeeks.org/convert-python-list-to-json/)
3. [How to append string in Python?](https://codedamn.com/news/python/append-string-in-python)
4. [How To Create And Use .env Files In Python](https://www.geeksforgeeks.org/how-to-create-and-use-env-files-in-python/)
5. [Python Functions](https://www.w3schools.com/python/python_functions.asp)
6. [Python - String Concatenation](https://www.w3schools.com/python/python_strings_concatenate.asp)
7. [Python | Remove empty strings from list of strings](https://www.geeksforgeeks.org/python-remove-empty-strings-from-list-of-strings/)

    Method 4: Using `filter()` is the most elegant and fastest way to perform this task. This method is highly recommended because *speed matters* when we deal with **large machine learning data set** that may potentially contain empty string.


### Quick Helpful Commands
1. To activate virtual environment in Windows, run:
    `venv\Scripts\activate`
