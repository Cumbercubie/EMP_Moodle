from __future__ import print_function

from googleapiclient.http import MediaIoBaseDownload

import DriveAPI
import io
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/spreadsheets']
global session
session = False
driveAPI = DriveAPI.auth(SCOPES, "credentials.json", "EMP Teacher's Moodle")
credentials = driveAPI.getCredentials()
service = build('drive', 'v3', credentials=credentials)
session = True

def listFiles():
    #Call the Drive v3 API
    results = service.files().list(
        pageSize=10,fields="nextPageToken,files(id,name)").execute()
    items = results.get('files',[])

    if not items:
        print('No files found')
    else:
        print("Files:")
        for item in items:
            print(u'{0} ({1})'.format(item['name'],item['id']))

def downloadFile(file_id,filepath):
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh,request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress()*100))
    with io.open(filepath,'wb') as f:
        fh.seek(0)
        f.write(fh.read())

def searchFolder(size,query):
    results = service.files().list(
        pageSize=size,fields="nextPageToken, files(id,name)",q=query).execute()
    items = results.get('files',[])
    if not items:
        print('No files found')
    else:
        print('Files:')
        for item in items:
            print('{0} ({1})'.format(item['name'],item['id']))
def createFolder(name):
    file_metadata = {
        'name':name,
        'mimeType':'application/vnd.google-apps.folder'
    }
    file = service.files().create(body=file_metadata,fields='id').execute()
    print('Folder ID: %s' % file.get('id'))

def main():
    searchFolder(10,"name='Classroom'")

if __name__ == '__main__':
    main()