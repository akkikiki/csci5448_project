# Communicates with each controller
import sys
from user_controller import UserController
from menu_controller import MenuController

class Driver():
    def __init__(self):
        self.user_controller = UserController()
        self.menu_controller = MenuController()

    def keyPressed(self, key):
        action = self.menu_controller.keyPressed(key)
        if action == "Show User Status":
            self.user_controller.updateView()

        elif action == "Save":
            self.user_controller.saveUser()

        elif action == "Load":
            self.user_controller.loadUser()

        elif action == "Change Name":
            name = input("New name >>  ")
            self.user_controller.changeName(name)
        else:
            print("WARNING: Not implemented yet")
            print()

