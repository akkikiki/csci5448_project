class MenuView():
    #UserData ud = UserData()

    def showActions(self, menu):
        print("----Menu---")
        for i, a in enumerate(menu.getActions()):
            print("%i) %s" % (i, a))
        print()

    def loginView(self):
        print("Username: ")
        user = input(" >>  ")
        print("Password: ")
        password = input(" >>  ")
        return user, password