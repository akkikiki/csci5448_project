from user import User
from user_view import UserView
from user_data import UserData
from menu import Menu

class UserController():
    def __init__(self):
        self._user_model = User("sample user", "pass")
        self._user_view = UserView()
        # self._view = Menu("Menusample_menu")

    def updateView(self):
        # self._view.showActionss()
        self._user_view.showStatus(self._user_model)
