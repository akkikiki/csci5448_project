from classifier import TextClassifier

class ClassifierController():
    def __init__(self):
        self._model = TextClassifier()

    def printParams(self):
        self._model.printParams()

    def tweakParams(self, param_indice, step_size):
        self._model.tweakParameters(param_indice, step_size)

    def resetParams(self):
        self._model.restart()

    def saveParams(self):
        self._model.save()

    def loadSate(self, indice):
        self._model.resumeState(indice)
