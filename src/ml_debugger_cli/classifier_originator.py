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
        state = copy(self._state)
        return Memento(state)

    def setMementoState(self, memento):
        self._state = memento.getState()

    def tweakParameters(self, param_indice, step_size):
        self._state[param_indice] = self._state[param_indice] + step_size