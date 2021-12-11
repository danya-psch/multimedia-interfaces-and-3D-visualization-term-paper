import os

class com_module:
    def __init__(self, file_path: str):
       self.file_path = file_path

    def transfer_data(self, data: str):
        self.fd = os.open(self.file_path, os.O_WRONLY | os.O_CREAT)
        self.pipe = os.fdopen(self.fd, 'wb', 0)
        self.pipe.write(data.encode())
        self.pipe.close()

    def __del__(self):
        self.pipe.close()
