from corpus import Corpus

# TODO: Implement factory design pattern

class CorpusController():
    def __init__(self):
        self._model = None

    def readCorpus(self, f_name):
        """
        Read the sentences from .txt or .xml file using Factory pattern
        :param f_name:
        :return:
        """
        self._model = Corpus().factory(f_name)
        self._model.read()

    def showCorpus(self):
        """
        Show the first 10 sentences from the read file.
        """
        if self._model.getTopLines():
            print(self._model.getTopLines())
        else:
            print("No corpus read yet")
