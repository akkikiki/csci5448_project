from menu import Menu

class MenuClassifier(Menu):
    def __init__(self):
        super(Menu, self).__init__()  # Calling the parent class constructor
        self._actions = ["Show Parameters", "Tweak Parameters", "Reset Tweaked Parameters", "Save Current Parameters"
            , "Load Previous State", "Exit"]