from menu import Menu

class MenuCorpus(Menu):
    def __init__(self):
        super(Menu, self).__init__()  # Calling the parent class constructor
        self._actions = ["Show sample sentences", "Read Corpus", "Undo", "Exit"]