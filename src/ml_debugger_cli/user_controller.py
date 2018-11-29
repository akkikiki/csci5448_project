from user import User
from user_view import UserView
from menu import Menu

class UserController():
    def __init__(self):
        self._user_model = User("Guest User", "No password for Guest User")
        self._user_view = UserView()
        # self._view = Menu("Menusample_menu")

    def updateView(self):
        """
        Show the details of the current user
        """
        self._user_view.showStatus(self._user_model)

    def changeName(self, name):
        """
        Change the name of the current user
        :param name: user name
        """
        self._user_model.setName(name)

    def changePassword(self, password):
        """
        Change the password of the current users
        :param password: user password
        """
        self._user_model.setPassword(password)

    def saveUser(self):
        """
        Save the current user
        """
        self._user_model.save()

    def loadUser(self):
        """
        Load the saved users
        """
        self._user_model.load()
