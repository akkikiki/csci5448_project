from menu import Menu
from menu_user import MenuUser
from menu_view import MenuView
import sys

class MenuController():
    def __init__(self):
        self._model = Menu()
        self._view = MenuView()

    def transitionUserMenu(self):
        self._model = MenuUser()

    def updateView(self):
        self._view.showActions(self._model)

    def getUserInput(self):
        return input("press the action number >> ")

    def logIn(self):
        user, password = self._view.loginView()

        if user in self._user_list:
            user_obj = self._user_list[user]
            if password == user_obj.getPassword():
                print("login successfull")
                self._user = user_obj


    def keyPressed(self, key):
        action = self._model.getKeyAction(key)
        if action == "User":
            self.transitionUserMenu()
        elif action == "Exit":
            sys.exit(1)
        else:
            return action

        return None
