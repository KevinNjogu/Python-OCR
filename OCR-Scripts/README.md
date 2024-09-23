# OCR Using Tesseract
### Fun Fact: The Tesseract OCR was made by the Google team & coincidentally, the Tesseract is the same cube shaped stone featured in the Marvel Cinematic universe popularized by Lokki.

## How to Install, Configure & Run this script
1. Open the CMD(Terminal) on your machine at the root of the project foler
2. Make sure you have Python installed (Python > 3.6)
3. Create a virtual environment by running `python3 -m venv venv`
    - This will create a virtual environment named **venv**
4. Run `source venv/bin/activate` on *Unix* OR `venv\Scripts\activate` on *Windows* to activate the environment.
    - Your terminal/cmd should have **(venv)** at the very start
5. Then run `pip install -r virtual_environment.txt` to install the dependencies.
    - The `-r` flag is to make the command persist installing the dependencies
6. Next, if you **do not have Tesseract installed as a stand-alone package**, follow the instructions in the resource below to install for your OS.
7. Once done, run `python ocr.py` to execute the file from the command line. 
    - Run line 7 incase running the file directly from your editor causes issues.


### Resources
1. [How to Build Optical Character Recognition (OCR) in Python](https://builtin.com/data-science/python-ocr)

### Helpful Tools
1. To activate virtual environment in Windows, run:
    `venv\Scripts\activate`
