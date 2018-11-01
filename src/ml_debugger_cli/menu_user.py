from menu import Menu

class MenuUser(Menu):
    def __init__(self):
        super(Menu, self).__init__()  # Calling the parent class constructor
        self._actions = ["Show User Status", "Change Name", "Change Password", "Save", "Load", "Exit"]