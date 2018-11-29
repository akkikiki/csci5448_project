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
        """
        Let the user log out
        """
        self._user = None
        print("logout successful")

    def getKeyAction(self, key):
        """
        Get the String of the action
        :param key: integer
        :return: action (String)
        """
        i = int(key)
        return self._actions[i]

    def doAction(self, context):
        """
        Save the menu to Context to go back one level up
        :param context: Context
        """
        context.setState(self)
