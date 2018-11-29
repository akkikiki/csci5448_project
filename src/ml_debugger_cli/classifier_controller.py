from classifier import TextClassifier

class ClassifierController():
    def __init__(self):
        self._model = TextClassifier()

    def printParams(self):
        """
        Output the current parameters
        """
        self._model.printParams()

    def tweakParams(self, param_indice, step_size):
        """
        Increment/Decrement the parameter of the specified indice by step_size
        :param param_indice: integer
        :param step_size: float value
        """
        self._model.tweakParameters(param_indice, step_size)

    def resetParams(self):
        """
        Reset the parameters to the default value
        """
        self._model.restart()

    def saveParams(self):
        """
        Save the current parameters
        """
        self._model.save()

    def loadSate(self, indice):
        """
        Load the parameters specified by the indice
        :param indice: integer
        """
        self._model.resumeState(indice)
