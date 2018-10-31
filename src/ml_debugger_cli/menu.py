import sys

class Menu():
    def __init__(self):
        self._actions = ["Data", "Model", "User", "Login", "Exit"]
        self._user = None

    def getActions(self):
        return self._actions

    def log_out(self):
        self._user = None
        print("logout successfull")

    def getKeyAction(self, key):
        i = int(key)
        return self._actions[i]
