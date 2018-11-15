# Communicates with each controller
import sys
from user_controller import UserController
from menu_controller import MenuController
from classifier_controller import ClassifierController

class Driver():
    def __init__(self):
        self.user_controller = UserController()
        self.menu_controller = MenuController()
        self.classifier_controller = ClassifierController()


    def keyPressed(self, key):
        action = self.menu_controller.keyPressed(key)
        action = self.keyPressedMenuData(key, action)
        if action:
            self.keyPressedMenuClassifier(key, action)

    def keyPressedMenuData(self, key, action):
        # Handle Menus Related to Data
        return action
        #return None  # successfully handled

    def keyPressedMenuClassifier(self, key, action):
        # Handle Menus Related to Classifier
        if action == "Show Parameters":
            self.classifier_controller.printParams()
        elif action == "Tweak Parameters":
            indice = int(input("Type the indice of param to tweak >> "))
            step_size = int(input("Type how much value to tweak a param >> "))
            self.classifier_controller.tweakParams(indice, step_size)

        elif action == "Reset Tweaked Parameters":
            self.classifier_controller.resetParams()
