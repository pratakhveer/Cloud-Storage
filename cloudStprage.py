import dropbox


class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken

    def uploadFiles(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.accessToken)
        f = open(fileFrom, "rb")
        dbx.files_upload(f.read(), fileTo)


def main():
    accessToken = "05E2BK9IMUgAAAAAAAAAAcC_svfgMN11bPZa7_2e6KWoSODJIIWiWtoigMWIAEzE"
    transferData = TransferData(accessToken)
    fileFrom = input("Enter the file path to transfer:")
    fileTo = input("Enter the full path to upload to Dropbox:")
    transferData.uploadFiles(fileFrom, fileTo)
    print("File has been moved")


main()
