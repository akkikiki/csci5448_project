class Memento():
    def __init__(self, state):
        self.state = state

    def getState(self):
        """
        Get the tracked state

        :return: list of float values (parameters)
        """
        return self.state
