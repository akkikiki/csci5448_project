
"""
This class should implement the factory design pattern to handle .xml and raw text files.

Reference: https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html
"""
import xml.etree.ElementTree as ET

class Corpus():
    def __init__(self):
        self._text = []
        self._f_name = ""

    def factory(t):
        if t.endswith("xml"):
            return XML(t)
        elif t.endswith("txt"):
            return RawText(t)
    factory = staticmethod(factory)

    # def readXML(self, f_name):
    #     assert f_name.endswith(".xml")
    #     self._f_name = f_name
    #     root = ET.parse(f_name)
    #     # assume that the real texts are surrounded by some kind of XML tags.
    #
    # def readRawText(self, f_name):
    #     self._f_name = f_name
    #     self._text = [line.strip() for line in open(f_name)]


class XML():
    def __init__(self, f_name):
        self._text = []
        self._f_name = f_name

    def read(self):
        assert self._f_name.endswith(".xml")
        root = ET.parse(self._f_name)
        for text in root.findall('text'):
            self._text.append(text.text)

    def getTopLines(self):
        return self._text[:10]



class RawText():
    def __init__(self, f_name):
        self._text = []
        self._f_name = f_name

    def read(self):
        self._text = [line.strip() for line in open(self._f_name)]

    def getTopLines(self):
        return self._text[:10]


