from user import User
from user_view import UserView
from menu import Menu

class UserController():
    def __init__(self):
        self._user_model = User("Guest User", "No password for Guest User")
        self._user_view = UserView()
        # self._view = Menu("Menusample_menu")

    def updateView(self):
        self._user_view.showStatus(self._user_model)

    def changeName(self, name):
        self._user_model.setName(name)

    def saveUser(self):
        self._user_model.save()

    def loadUser(self):
        self._user_model.load()
