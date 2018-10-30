class MenuView():
    #UserData ud = UserData()

    def showActions(self, menu):
        for i, a in enumerate(menu.getActions()):
            print(i, a)