from GoogleAPI import GoogleAPI

class Sheets:
    def __init__(self,id):
        api = GoogleAPI('sheets')
        self.service = api.service
        self.id = id
    # def getStudentList(self):
    #     RANGES = 'Class!A2:A16'
    #     sheet = self.service.spreadsheets()
    #     result = sheet.values().get(spreadsheetId=self.id,
    #                                 range=RANGES).execute()
    #     values = result.get('values', [])
    #     student = []
    #     for i in values:
    #         student.append(i[0])
    #     return student
    def getData(self, startCell = 'A1', endCell = 'A'):
        '''@param startCell means cell that you start to get Data, same with endCell

            return List[List[String]]
        '''
        RANGES = 'Class!{}:{}'.format(startCell,endCell)
        sheet =self.service.spreadsheets()
        result = sheet.values().get(spreadsheetId=self.id,range=RANGES).execute()
        #List[List[String]]
        values = result.get('values', [])
        return values
