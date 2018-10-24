from user import User
from collections import defaultdict

class UserData():
    def __init__(self, name):
        self.name = name
        self._userList = defaultdict(User)
        self.addGuestUser()

    def addGuestUser(self):
        self._userList["Guest"] = User("guest", "guest")

    def showActions(self):
        return self._actions
