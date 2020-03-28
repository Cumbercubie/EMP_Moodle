from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import  Request
import GoogleAuth
import GoogleFactory
SCOPES = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/spreadsheets']
class SheetService:
    def __init__(self,service): 
        self.service = service
        # sheetAPI = GoogleAuth.auth(SCOPES, "credentials.json", "EMP Teacher's Moodle")
        # credentials = sheetAPI.getCredentials()
        # service = build('sheets', 'v4', credentials=credentials)
    def createSheet(self,title):
        spreadsheet = {
            'properties': {
                'title': title
            }
        }
        spreadsheet = self.service.spreadsheets().create(body=spreadsheet, fields='spreadsheetId').execute()
        return spreadsheet
    def getSheetById(self,sheetId,range_name):
        print(sheetId)
        sheet = self.service.spreadsheets().values().get(spreadsheetId=sheetId,range=range_name).execute()
        rows = sheet.get('values',[])
        print(rows)

    def readSheetByName(self,title,row,column):
        print('cannot read')
    def getAllRows(self,sheetId,sheet_name,start_cells,last_column):
        range_name = sheet_name+'!'+start_cells+':'+last_column
        sheet = self.service.spreadsheets()
        result = sheet.values().get(spreadsheetId=sheetId,
                                    range=range_name).execute()
        values = result.get('values', [])
        if not values:
            print('No data found.')
        else:
            print('Name, Major:')
            for row in values:
                # Print columns A and E, which correspond to indices 0 and 4.
                print('%s, %s' % (row[0], row[3]))
def main():
    print("hello")
if __name__ == '__main__':
    main()




