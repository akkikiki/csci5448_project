
"""
This class should implement the factory design pattern to handle .xml and raw text files.

"""
import xml.etree.ElementTree as ET

class Corpus():
    """
    The implementation thsi class is referred from https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html
    """
    def __init__(self):
        self._text = []
        self._f_name = ""

    def factory(t):
        """
        (static) Factory method
        :param t: String of the file name
        :return: XML or RawText depending on the file
        """
        if t.endswith("xml"):
            return XML(t)
        elif t.endswith("txt"):
            return RawText(t)
    factory = staticmethod(factory)



class XML():
    def __init__(self, f_name):
        self._text = []
        self._f_name = f_name

    def read(self):
        """
        Read the sentences from a file
        """
        assert self._f_name.endswith(".xml")
        root = ET.parse(self._f_name)
        for text in root.findall('text'):
            self._text.append(text.text)

    def getTopLines(self):
        """
        Obtain the first 10 lines from the read corpus
        :return: 10 lines of Strings
        """
        return self._text[:10]


class RawText():
    def __init__(self, f_name):
        self._text = []
        self._f_name = f_name

    def read(self):
        """
        Read the sentences from a file
        """
        self._text = [line.strip() for line in open(self._f_name)]

    def getTopLines(self):
        """
        Obtain the first 10 lines from the read corpus
        :return: 10 lines of Strings
        """
        return self._text[:10]


