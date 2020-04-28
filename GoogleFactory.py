import GoogleAuth
from abc import ABCMeta, abstractclassmethod
import io
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from googleapiclient.discovery import build
SCOPES = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/spreadsheets']
class GoogleAPIFactory:
    @staticmethod
    def get_API(API_type):
        API_type.lower()
        credentials = GoogleAuth.auth(SCOPES, 'credentials.json', 'MoodleForEMP')
        try:
            if API_type == "drive":
                service = build('drive', 'v3', credentials=credentials)
                return service
            if API_type == "sheet":
                service = build('sheet', 'v3', credentials=credentials)
                return service
            raise AssertionError('API not found')
        except AssertionError as _e:
            print(_e)

