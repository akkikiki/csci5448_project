from user_data import UserData

class Menu():
    def __init__(self):
        self._actions = ["Data", "Model", "Show status", "Login", "Exit"]
        self._user = None
        # self._user_data = UserData(name)
        # self.showActions()

        # action = input("press the action number >> ")
    def getActions(self):
        return self._actions

    def showActions(self):
        for i, a in enumerate(self._actions):
            print(i, a)

    def showStatus(self):
        print("User: " + self._user.getName())

    def login(self):
        print("Username: ")
        user = input(" >>  ")
        print("Password: ")
        password = input(" >>  ")
        if user in self._user_list:
            user_obj = self._user_list[user]
            if password == user_obj.getPassword():
                print("login successfull")
                self._user = user_obj
        # self._user =

    def logOut(self):
        self._user = None
        print("logout successfull")
