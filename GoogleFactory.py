import DriveAPI
import io
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from googleapiclient.discovery import build
SCOPES = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/spreadsheets']
class GoogleAPIFactory:
    @staticmethod
    def get_API(API_type):
        API_type = 
        creds = DriveAPI.auth(SCOPES,'credentials.json','MoodleForEMP')
        try:
            if API_type == "Drive":
                service = build('drive', 'v3', credentials=credentials)
                return service
            if API_type == "Sheet":
                service = build('sheet', 'v3', credentials=credentials)
                return service

