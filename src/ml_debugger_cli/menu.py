"""
Class for menu
"""

class Menu():
    def __init__(self):
        self._actions = ["Corpus", "Model", "User", "Exit"]
        self._user = None

    def getActions(self):
        return self._actions

    def log_out(self):
        self._user = None
        print("logout successful")

    def getKeyAction(self, key):
        i = int(key)
        return self._actions[i]
