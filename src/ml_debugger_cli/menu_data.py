from menu import Menu

class MenuData(Menu):
    def __init__(self):
        super(Menu, self).__init__()  # Calling the parent class constructor
        self._actions = ["Show Status", "Tweak Parameters", "Save", "Load", "Exit"]
