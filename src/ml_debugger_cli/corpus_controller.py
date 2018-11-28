from corpus import Corpus

# TODO: Implement factory design pattern

class CorpusController():
    def __init__(self):
        self._model = None

    def readCorpus(self, f_name):
        # Implement Factory pattern here
        self._model = Corpus().factory(f_name)
        self._model.read()

        #if f_name.endswith(".xml"):
        #    self._model.readXML(f_name)
        #else:
        #    self._model.readRawText(f_name)

    def showCorpus(self):
        if self._model.getTopLines():
            print(self._model.getTopLines())
        else:
            print("No corpus read yet")
