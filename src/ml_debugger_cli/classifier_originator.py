from classifier_memento import Memento
from copy import copy

class Originator():
    def __init__(self):
        self._state = None  # current params

    def getState(self):
        return self._state

    def setState(self, state):
        self._state = state

    def saveState(self):
        """
        Save the current parameters as a separate Memento
        :return: Memento
        """
        state = copy(self._state)
        return Memento(state)

    def setMementoState(self, memento):
        """
        Convert Memento to State (list of float values)
        :param memento: Memento
        """
        self._state = memento.getState()

    def tweakParameters(self, param_indice, step_size):
        """

        :param param_indice:
        :param step_size: float value to increment/decrement the parameter
        :return:
        """
        self._state[param_indice] = self._state[param_indice] + step_size