# Handles how to display the user
from user import User

class UserView():
    #UserData ud = UserData()

    def showStatus(self, user):
        print("-------")
        print("User Name = " + user.getName())
        print("Password = " + user.getPassword()) # may not want this
        print("Permission Level = " + user.getPermission())
        print("-------")
        print()

