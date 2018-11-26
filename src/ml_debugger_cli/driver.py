# Communicates with each controller
import sys
from user_controller import UserController
from menu_controller import MenuController
from classifier_controller import ClassifierController
from corpus_controller import CorpusController

class Driver():
    def __init__(self):
        self.user_controller = UserController()
        self.menu_controller = MenuController()
        self.classifier_controller = ClassifierController()
        self.corpus_controller = CorpusController()


    def keyPressed(self, key):
        """
        Handle the key pressed by the user

        :param key: Keyboard key
        """
        action = self.menu_controller.keyPressed(key)
        if action:
            action = self.keyPressedMenuCorpus(action)
        if action:
            self.keyPressedMenuClassifier(action)

    def keyPressedMenuCorpus(self, action):
        if action == "Show sample sentences":
            self.corpus_controller.showCorpus()
        elif action == "Read Corpus":
            f_name = input("Specify the path to the corpus >> ")
            self.corpus_controller.readCorpus(f_name)
        else:
            return action


    def keyPressedMenuClassifier(self, action):
        """
        Handle keys related to the Classifier class
        :param action: The corresponding action string
        :return:
        """
        # Handle Menus Related to Classifier
        if action == "Show Parameters":
            self.classifier_controller.printParams()

        elif action == "Tweak Parameters":
            indice = int(input("Type the indice of param to tweak >> "))
            step_size = int(input("Type how much value to tweak a param >> "))
            self.classifier_controller.tweakParams(indice, step_size)

        elif action == "Save Current Parameters":
            self.classifier_controller.saveParams()
            #print(len(self.classifier_controller._model._care_taker._mementos))

        elif action == "Reset Tweaked Parameters":
            self.classifier_controller.resetParams()

        elif action == "Load Previous State":
            indice = int(input("Type the indice of state you want to load >> "))
            self.classifier_controller.loadSate(indice)

