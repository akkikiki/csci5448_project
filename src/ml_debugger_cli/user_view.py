# Handles how to display the user
from user import User

class UserView():

    def showStatus(self, user):
        """
        Show the information of a given user
        :param user: User
        """

        print("-------")
        print("User Name = " + user.getName())
        print("Password = " + user.getPassword()) # may not want this
        print("Permission Level = " + user.getPermission())
        print("-------")
        print()

