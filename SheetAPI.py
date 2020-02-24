class SheetService:
    def __init__()
    def createSheet(title):
        spreadsheet = {
            'properties': {
                'title': title
            }
        }
        spreadsheet = sheet_service.spreadsheets().create(body=spreadsheet, fields='spreadsheetId').execute()
        return spreadsheet
    def alternative_sheet(title,row,column):
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secrets.json',SCOPES)
        client = gspread.authorize(creds)
        try:
            return client.open('Data for mail merge').worksheet(title)
        except:
            print('Sheet not exists')
            return client.open('Data for mail merge').add_worksheet(title, row, column)


