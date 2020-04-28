from GoogleAPI import GoogleAPI
from googleapiclient.http import MediaIoBaseDownload
from SheetsAPI import Sheets
import io
class Drive:
    def __init__(self):
        api = GoogleAPI('drive')
        self.service = api.service
    def getFilesList(self):
        service = self.service
        try:
            results = service.files().list(pageSize=1000, fields="nextPageToken, files(id, name)").execute()
            items = results.get('files', [])
            return items
        except Exception as e:
            print("Something went wrong!")
            return None

    def createFolder(self, name = 'folders', parent = []):
        #folders ở đây được coi như 1 file
        #tạo metadata cho file với name bằng name truyền vào, mimeType là thuộc tính của file ở đây đối với folders thì mặc định là  'application/vnd.google-apps.folder'
        #Hàm sẽ return file đã tạo để thực hiện một số công việc khác trong Flask nếu có, không thì bỏ việc return bằng cách _ = obj.createFolders(name,parent)

        service = self.service
        metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': parent
        }
        file = service.files().create(body=metadata, fields = 'id').execute()
        print ('Folder ID: {}'.format(file.get('id')))
        return file
    def createFolderTree(self, name = 'untitled', students = []):
        # students = ['Votiendung','Caothienhuan','Vuduchuy']
        parent = self.createFolder(name = name)
        parent_id = parent.get('id')
        print(parent_id)
        for student in students:
            self.createFolder(name=student,parent = [parent_id])
	#del sheets


    def insertResultFileToFolders(self,folder):
        folder_id = folder.get('id')
        metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.spreadsheet',
            'parent': [folder_id]
        }
        file = self.service.files().create(body=metadata,fields='id').execute()
        print('File uploaded and inserted in to {}'.format(folder.get('name')))
        return file
    def searchFiles(self, name):
        #result được trả về sẽ là kiểu list mà mỗi phần tử là dạng files.
        #Trường hợp tìm không thấy sẽ trả về list rỗng, có thể sẽ xảy ra Index out of range, Exception
        #Hàm này có param là name, tức là search theo tên, trường hợp nhiều file hay folder trùng tên thì nó sẽ trả về nhiều kết quả, cẩn thận khi sử dụng

        queries = "mimeType='application/vnd.google-apps.folder'"
        spaces = 'drive'
        reponse = self.service.files().list(q=queries,spaces=spaces,fields='nextPageToken, files(id,name)').execute()
        filesList = reponse.get('files',[])
        result = []
        for file in filesList:
            if file.get('name') == name:
                result.append(file)
        return result
    def uploadFiles(self):
        #Chắc vẫn sẽ chưa viết vì tình hình là những thứ được upload sẽ là file kết quả, thì files kết quả này là file nên dùng hàm insertResultFileToFolders để có thể uploads thẳng file này lên trên một thư mục nào đó cố định
        #Nếu cần thì bảo em em viết thêm vào cho nên là khỏi lo ha :v
        pass
    def downloadFile(self, file):
        #Hàm dùng để download một file nhưng chả biết nó sẽ lưu ở đâu trên server cả :) ? Cái này chắc nhờ anh quá :v em thì chịu đấy :)))
        type = file.get('mimeType')
        file_id = file.get('id')
        try:
            request = self.service.files().get_media(fileId=file_id)
        except:
            request = self.service.files().get_media(fileId=file_id)
        finally:
            print('Can not recognize mimeType')
            return None

        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Download %d%%." % int(status.progress() * 100))
    def getChange(self):
        pass
