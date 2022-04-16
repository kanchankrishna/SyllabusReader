#Type "help", "copyright", "credits" or "license()" for more information.
from PIL import Image
from flask import render_template
import pickle
import pytesseract
import sys
import json
from dateutil import parser

#Connect to Google Calender API
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

scopes = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
credentials = flow.run_console()
pickle.dump(credentials, open("token.pkl", "wb")) 
credentials = pickle.load(open("token.pkl", "rb"))
service = build("calendar", "v3", credentials=credentials)
result = service.calendarList().list().execute()
#print("gcal list:", result)
#see calendar events
calendar_id = result['items'][0]['id']
result = service.events().list(calendarId=calendar_id).execute()
#print(result['items'][0])

# Refer to the Python quickstart on how to setup the environment:
# https://developers.google.com/calendar/quickstart/python
# Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
# stored credentials.

#testing standard event - works



# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/5.1.0/bin/tesseract'

custom_oem_psm_config = r'--psm 3'

#Get user input (their file path of the image) from the command line
image_name = sys.argv[1]

# Simple image to string using command line arguments
#print(pytesseract.image_to_string(Image.open('/Users/kanchu/Desktop/SampleSyllabus.jpg'), config=custom_oem_psm_config))
print("printing the image")
print(pytesseract.image_to_string(Image.open(image_name), config=custom_oem_psm_config))

output_string = pytesseract.image_to_string(Image.open(image_name), config=custom_oem_psm_config)
#print(output_string)
#Put string into a txt file
#text_file = open("sample.txt", "w")
#n = text_file.write(output_string)
#text_file.close()
output_string = output_string.strip().split('\n')
#output string is like an array of string for each line

#Create a list of key words to look for
#key_words = ["Assignment", "Homework", "Exam", "Date", "Test", "Quiz", "Midterm", "Due"]
key_words = ["Assignment", "Homework", "Exam", "Test", "Quiz", "Midterm", "Due"]

#Read file line by line in Python
file1 = open("sample.txt", 'r')
lines = file1.readlines()
 
first_line = lines[0]
#Parse by space and add to dictionary (like a map)
#print (first_line)

class my_dictionary(dict):
  
    # __init__ function
    def __init__(self):
        self = dict()
          
    # Function to add key:value
    def add(self, key, value):
        self[key] = value
  
# Main Function
dict_obj = my_dictionary()

#fix input validation later
#first_line_words = first_line.split(' ')
#length_first_line = len(first_line_words)
#print("printing" , first_line_words)
#print(length_first_line)

print("number of lines: ", len(lines))
#i = 1;
for i in range(1, (len(lines))):
    line = lines[i]
    list_of_line_words = line.split(' ')
    length_list_of_line_words = len(list_of_line_words)
    last_ele_date = list_of_line_words[-1]
    #could use -1 for last index
    last_ele_date = last_ele_date.strip('\n')
    #print(last_ele_date, "potential new string")
    # initializing format
    format = "%d/%m/%Y"
 
    # checking if format matches the date
    res = True
 
    # using try-except to check for truth value
    try:
        res = bool(parser.parse(last_ele_date))
    except ValueError:
        res = False
    #print(res)
    #now concatenate rest of string to be the key value in the dictionary object by iterating through the line
    assignment_type = ""
    for j in range(0, (length_list_of_line_words - 1)):
        assignment_type += list_of_line_words[j]
    #print (assignment_type)
    #will print false for the last line
    #print(i)
    #print(list_of_line_words)
    dict_obj.add(assignment_type, last_ele_date)
    #var1 = last_ele_date
    #string_var1 = str(last_ele_date)
    var2 = "T09:00:00-07:00"
    var3 = "".join([last_ele_date, var2])
    print("this is var3", var3)
    #test_date = '2022-04-15T09:00:00-07:00'
    event = {
  'summary': assignment_type,
  'location': '800 Howard St., San Francisco, CA 94103',
  #'description': 'A chance to hear more about Google\'s developer products.',
  'start': {
    'dateTime': var3,
    'timeZone': 'America/Los_Angeles',
  },
  'end': {
    #'dateTime': '2022-04-15T09:00:00-07:00',
    'dateTime': var3,
    'timeZone': 'America/Los_Angeles',
  },
  #'recurrence': [
    #'RRULE:FREQ=DAILY;COUNT=2'
  #],
  'attendees': [
    {'email': 'lpage@example.com'},
    {'email': 'sbrin@example.com'},
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}
    service.events().insert(calendarId='primary', body=event).execute()



print("Dictionary below: ")
print(dict_obj)

# Serializing json  
json_object = json.dumps(dict_obj, indent = 4) 
print(json_object)


#Create an empty dictionary to be populated (similar to a map in Java/C++)
Dict = {}
#Read a string line by line
#for idx in range(0, len(output_string)):
    #if (output_string[idx] == 'Assignment'

#@app.route("/")
#def index():
    #return render_template("home.html")






