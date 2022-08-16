from PIL import Image
import pytesseract
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

scopes = ['https://www.googleapis.com/auth/calendar']
secret_client_file = "client_secret_2.json"
flow = InstalledAppFlow.from_client_secrets_file(secret_client_file, scopes=scopes)
credentials = flow.run_console()
service = build("calendar", "v3", credentials=credentials)
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/5.0.1/bin/tesseract'

custom_oem_psm_config = r'--psm 3'

image_name = "nowusethis.jpg"

# Simple image to string using command line arguments
print("printing the image")

output_string = pytesseract.image_to_string(Image.open(image_name), config=custom_oem_psm_config)
print(output_string)

#Create a list of key words to look for
key_words = ["Assignment", "Homework", "Exam", "Test", "Quiz", "Midterm", "Due"]

lines = output_string.strip().split('\n')
title = output_string[0]
for line in lines[1:]:
    summary = title + ": " + line.split()[:-1]
    date = line.split()[-1]
    start_date = date + "T00:00:00-07:00"
    end_date = date + "T12:00:00-07:00"
    event_dict = {
        'summary': summary,
        'start': {
            'dateTime': start_date,
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': end_date,
            'timeZone': 'America/Los_Angeles',
        },
    }

    service.events().insert(calendarId='primary', body=event_dict).execute()
    break

#fix input validation later
#first_line_words = first_line.split(' ')
#length_first_line = len(first_line_words)
#print("printing" , first_line_words)
#print(length_first_line)

# lines = {}
#
# print("number of lines: ", len(lines))
# #i = 1;
# for i in range(1, (len(lines))):
#     line = lines[i]
#     list_of_line_words = line.split(' ')
#     length_list_of_line_words = len(list_of_line_words)
#     last_ele_date = list_of_line_words[length_list_of_line_words - 1]
#     last_ele_date = last_ele_date.strip('\n')
#     #print(last_ele_date, "potential new string")
#     # initializing format
#     format = "%d/%m/%Y"
#
#     # checking if format matches the date
#     res = True
#
#     # using try-except to check for truth value
#     try:
#         res = bool(parser.parse(last_ele_date))
#     except ValueError:
#         res = False
#     #print(res)
#     #now concatenate rest of string to be the key value in the dictionary object by iterating through the line
#     assignment_type = ""
#     for j in range(0, (length_list_of_line_words - 1)):
#         assignment_type += list_of_line_words[j]
    #print (assignment_type)
    #will print false for the last line
    #print(i)
    #print(list_of_line_words)
    # dict_obj.add(assignment_type, last_ele_date)
    # #var1 = last_ele_date
    # #string_var1 = str(last_ele_date)
    # var2 = "T09:00:00-07:00"
    # var3 = "".join([last_ele_date, var2])
    # print("this is va
