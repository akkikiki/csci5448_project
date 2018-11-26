"""
Class for a text classifier
"""

from copy import copy
from classifier_originator import Originator
from classifier_caretaker import CareTaker
import numpy as np

class TextClassifier():
    def __init__(self):
        self._originator = Originator()
        self._care_taker = CareTaker()

        self._tweaks = 0  # keeping track of how many times did I tweak
        #self._params = None
        self.initDefualt()


    def initDefualt(self):
        params = np.zeros(5, dtype=float)
        self._originator.setState(params)
        self.save() # saving initial state
        # print(self._care_taker.getMoments(0).getState())

    def tweakParameters(self, param_indice, step_size):
        """
        Tweak the specified parameter of the classifier

        :param param_indice: indice of the parameter to tweak
        :param step_size: value of how much you want to tweak
        :return:
        """
        self._originator.tweakParameters(param_indice, step_size)
        self._tweaks += 1

    def save(self):
        """
        Temporary save the current parameters
        """
        momento = self._originator.saveState()
        self._care_taker.addState(momento)

    def resumeState(self, indice):
        """
        Resume to the parameters at the checkpoint specified by the indice.

        :param indice: ith checkpoint
        :return:
        """
        self._originator.setMementoState(self._care_taker.getMoments(indice))

    def restart(self):
        """
        Reset all parameters to the default i.e., before tweaked by the user

        :return:
        """
        memento = self._care_taker.getMoments(0)
        self._originator.setMementoState(memento)

    def printParams(self):
        print(self._originator.getState())

if __name__ == "__main__":
    classifier = TextClassifier()
    classifier.initDefualt()
    classifier.printParams()
    classifier.tweakParameters(0, 5)
    classifier.printParams()
