class User():
    def __init__(self, name, password):
        self._name = name
        self._password = password
        self._permission_level = "General"  # General or Admin

    def getPassword(self):
        return self._password

    def getName(self):
        return self._name

    def getPermission(self):
        return self._permission_level

    def setPermission(self, permission):
        self._permission_level = permission
