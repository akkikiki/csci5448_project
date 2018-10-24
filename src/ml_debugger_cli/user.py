class User():
    def __init__(self, name, password):
        self._name = name
        self._password = password

    def getPassword(self):
        return self._password
