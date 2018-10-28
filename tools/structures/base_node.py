
class BaseNode():
    def __init__(self, data):
        self.data = data
        self.status = BaseNode.BLANK

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return self.__str__()

BaseNode.BLANK = 'BLANK'
BaseNode.COMPLETED = 'COMPLETED'
BaseNode.PENDING = 'PENDING'
