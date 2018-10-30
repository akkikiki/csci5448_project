# Handles how to display the user
from user import User

class UserView():
    #UserData ud = UserData()

    def showStatus(self, user):
        print("UserName = " + user.getName())
        print("Password = " + user.getPassword()) # may not want this
        print("Permission Level = " + user.getPermission()) # may not want this

