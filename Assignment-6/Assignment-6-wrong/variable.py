class INTEGER():
    name = ''
    value = None
    varType = 'INTEGER'

    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def getType(self):
        return self.varType

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
        return self.value

class BOOLEAN():
    name = ''
    value = None
    varType = 'BOOLEAN'

    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def getType(self):
        return self.varType

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
        return self.value

