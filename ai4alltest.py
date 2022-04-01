#Type "help", "copyright", "credits" or "license()" for more information.
from PIL import Image
from flask import render_template

import pytesseract
import sys

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/5.1.0/bin/tesseract'

custom_oem_psm_config = r'--psm 3'

#Get user input (their file path of the image) from the command line
image_name = sys.argv[1]

# Simple image to string using command line arguments
#print(pytesseract.image_to_string(Image.open('/Users/kanchu/Desktop/SampleSyllabus.jpg'), config=custom_oem_psm_config))
print(pytesseract.image_to_string(Image.open(image_name), config=custom_oem_psm_config))

output_string = pytesseract.image_to_string(Image.open(image_name), config=custom_oem_psm_config)
print(output_string)
#Put string into a txt file
text_file = open("sample.txt", "w")
n = text_file.write(output_string)
text_file.close()


#Create a list of key words to look for
key_words = ["Assignment", "Homework", "Exam", "Test", "Quiz", "Midterm"]

#Read file line by line in Python
file1 = open("sample.txt", 'r')
lines = file1.readlines()
 
first_line = lines[0]
#Parse by space and add to dictionary (like a map)
print (first_line)

class my_dictionary(dict):
  
    # __init__ function
    def __init__(self):
        self = dict()
          
    # Function to add key:value
    def add(self, key, value):
        self[key] = value
  
# Main Function
dict_obj = my_dictionary()

first_line_words = first_line.split(' ')
for word in first_line_words:
    if not(word in key_words):
        print("invalid input")

i = 1;
for i in range(len(lines)):
    line = lines[i]
    list_of_line_words = line.split(' ')
    dict_obj.add(list_of_line_words[0], list_of_line_words[1])

print("Dictionary below: ")
print(dict_obj)


#Create an empty dictionary to be populated (similar to a map in Java/C++)
Dict = {}
#Read a string line by line
#for idx in range(0, len(output_string)):
    #if (output_string[idx] == 'Assignment'

@app.route("/")
def index():
    return render_template("home.html")




