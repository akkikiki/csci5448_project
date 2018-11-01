import json

class User():
    def __init__(self, name, password):
        self._name = name
        self._password = password
        self._permission_level = "General"  # General or Admin

    def getPassword(self):
        return self._password

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getPermission(self):
        return self._permission_level

    def setPermission(self, permission):
        self._permission_level = permission

    def setPassword(self, password):
        self._password = password

    def load(self):
        data = json.load(open("data/user_data.json"))
        self.setName(data["name"])
        self.setPassword(data["password"])
        self.setPermission(data["permission"])

    def save(self):
        data = {}
        data["name"] = self._name
        data["password"] = self._password
        data["permission"] = self._permission_level
        json.dump(data, open("data/user_data.json", "w"))
