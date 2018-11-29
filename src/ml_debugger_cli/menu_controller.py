from menu import Menu
from menu_classifier import MenuClassifier
from menu_data import MenuData
from menu_corpus import MenuCorpus
from menu_user import MenuUser
from menu_view import MenuView
from menu_context import Context
import sys

class MenuController():
    def __init__(self):
        self._model = Menu()
        self._view = MenuView()
        self._context = Context()

    def transitionUserMenu(self):
        """
        Transition to the menu related to Users
        """
        self._model.doAction(self._context)
        self._model = MenuUser()

    def transitionCorpusMenu(self):
        """
        Transition to the menu related to Corpus
        """
        self._model.doAction(self._context)
        self._model = MenuCorpus()

    def transitionClassifierMenu(self):
        """
        Transition to the menu related to Classifier
        """

        self._model.doAction(self._context)
        self._model = MenuClassifier()

    def updateView(self):
        """
        Update the view
        """
        self._view.showActions(self._model)

    def getUserInput(self):
        """
        Get the user's action item
        :return: integer input of the user
        """
        return input("press the action number >> ")

    def logIn(self):
        """
        Log in the user
        :return:
        """
        user, password = self._view.loginView()

        if user in self._user_list:
            user_obj = self._user_list[user]
            if password == user_obj.getPassword():
                print("login successfull")
                self._user = user_obj


    def keyPressed(self, key):
        """
        Handles the action items related to the top level menu
        :param key: integer
        :return: action item
        """
        action = self._model.getKeyAction(key)
        if action == "User":
            self.transitionUserMenu()

        elif action == "Corpus":
            self.transitionCorpusMenu()

        elif action == "Model":
            self.transitionClassifierMenu()

        elif action == "Undo":
            self._model = self._context.getState()

        elif action == "Exit":
            sys.exit(1)
        else:
            return action

        return None
