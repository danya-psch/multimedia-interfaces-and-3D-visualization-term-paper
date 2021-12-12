class RequestMessage:
    message = ['0', '0', '0', '0']

    def __init__(self):
        pass

    def add(self, value, position):
        self.message[position] = value

    def top(self):
        return self.message[len(self.message) - 1]

    def pop(self):
        self.message.pop()

    def serialize(self):
        return  '|'.join([str(i) for i in self.message])
