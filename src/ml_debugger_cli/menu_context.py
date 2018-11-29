class Context():
    def __init__(self):
        self._state = None

    def setState(self, state):
        """
        Getters for the Context class
        :param state:
        """
        self._state = state

    def getState(self):
        """
        Setters for the Context class
        :return: State
        """
        return self._state
