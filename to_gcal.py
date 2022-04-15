# Connect to Google Calender API
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

scopes = ['https://www.googleapis.com/auth/calendar']
secret_client_file = "client_secret_2.json"
flow = InstalledAppFlow.from_client_secrets_file(secret_client_file, scopes=scopes)
credentials = flow.run_console()
service = build("calendar", "v3", credentials=credentials)

event = {
  'summary': "assignment_type",
  'location': '800 Howard St., San Francisco, CA 94103',
  'description': 'A chance to hear more about Google\'s developer products.',
  'start': {
    'dateTime': '2022-05-15T08:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'end': {
    'dateTime': '2022-05-15T09:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
}
service.events().insert(calendarId='primary', body=event).execute()





