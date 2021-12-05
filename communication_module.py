import os

class com_module:
    def __init__(self, file_path: str):
        self.fd = os.open(file_path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC )
        self.pipe = os.fdopen(self.fd, 'wb', 0)

    def transfer_data(self, data: str):
        self.pipe.write(data.encode())

    def __del__(self):
        self.pipe.close()
