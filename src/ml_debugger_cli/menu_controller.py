from menu import Menu
from menu_view import MenuView

class MenuController():
    def __init__(self):
        self._model = Menu()
        self._view = MenuView()

    def updateView(self):
        self._view.showActions(self._model)

    def getUserInput(self):
        action = input("press the action number >> ")
