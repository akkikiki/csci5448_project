# Communicates with each controller

from user_controller import UserController
from menu_controller import MenuController

class Driver():
    def __init__(self):
        self.user_controller = UserController()
        self.menu_controller = MenuController()
