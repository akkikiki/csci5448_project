class CareTaker():
    def __init__(self):
        self._mementos = []  # keeping track of the states

    def addState(self, state):
        """
        Save the memento
        :param state:
        """
        self._mementos.append(state)

    def getMemento(self, indice):
        """
        Returns the Memento at the specified indice

        :param indice: The indice of the memento you saved
        :return: Memento
        """
        return self._mementos[indice]
