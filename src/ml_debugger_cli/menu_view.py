class MenuView():

    def showActions(self, menu):
        """
        Show the action items
        :param menu: Menu
        """
        print("----Menu---")
        for i, a in enumerate(menu.getActions()):
            print("%i) %s" % (i, a))
        print()

    def loginView(self):
        """
        Show the view when a user wants to login
        :return:
        """
        print("Username: ")
        user = input(" >>  ")
        print("Password: ")
        password = input(" >>  ")
        return user, password