from __future__ import print_function
import requests
from googleapiclient.http import MediaIoBaseDownload

import GoogleAuth
import io
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/spreadsheets']
global session
session = False
driveAPI = GoogleAuth.auth(SCOPES, "credentials.json", "EMP Teacher's Moodle")
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


def getChanges():
    saved_start_page_token = service.changes().getStartPageToken().execute().get('startPageToken')
    while True:
        page_token = saved_start_page_token
        while page_token is not None:
            response = service.changes().list(pageToken=page_token,
                                              spaces='drive').execute()
            for change in response.get('changes'):
                # Process change
                fileId = change.get('fileId')
                file = service.files().get(fileId=fileId,fields='parents')
                print('Change found for file: {}   remove: {}, at {}, parent: {}'.format(change.get('fileId'), change.get('kind'),
                                                                             change.get('time'),file['parents']))
            if 'newStartPageToken' in response:
                # Last page, save this token for the next polling interval
                saved_start_page_token = response.get('newStartPageToken')
            page_token = response.get('nextPageToken')

def main():
    # start_token = service.changes().getStartPageToken().execute()
    # print('Start token: %s' % start_token.get('startPageToken'))
    # getChanges()
    # file = service.files().get(fileId='1Eiz_rMNNRu6-BXiMcY03JaaC1gNdBqB_R7gUfwR0Ijk',fields='parents').execute()
    # parents = file['parents']
    # print(parents)
    listFiles()

if __name__ == '__main__':
    main()