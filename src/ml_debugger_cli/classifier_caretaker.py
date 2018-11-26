class CareTaker():
    def __init__(self):
        self._mementos = []  # keeping track of the states

    def addState(self, state):
        """
        Save the memento
        :param state:
        """
        self._mementos.append(state)

    def getMoments(self, indice):
        return self._mementos[indice]
