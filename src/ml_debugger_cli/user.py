import json

class User():
    def __init__(self, name, password):
        self._name = name
        self._password = password
        self._permission_level = "General"  # General or Admin

    def getPassword(self):
        """
        Getter for the password
        :return: pasword
        """
        return self._password

    def getName(self):
        """
        Getter for the user name
        :return: user name
        """
        return self._name

    def setName(self, name):
        """
        Setter for the user name
        :param name: user name
        """
        self._name = name

    def getPermission(self):
        """
        Getter for the permission level
        :return: permission level
        """
        return self._permission_level

    def setPermission(self, permission):
        """
        Changing the permission level of a user
        :param permission: Admin or General
        :return:
        """
        self._permission_level = permission

    def setPassword(self, password):
        """
        Setting a new password
        :param password: String
        """
        self._password = password

    def load(self):
        """
        Load all of the user information
        """
        data = json.load(open("data/user_data.json"))
        self.setName(data["name"])
        self.setPassword(data["password"])
        self.setPermission(data["permission"])

    def save(self):
        """
        Save the current user information to an external JSON file
        """
        data = {}
        data["name"] = self._name
        data["password"] = self._password
        data["permission"] = self._permission_level
        json.dump(data, open("data/user_data.json", "w"))
