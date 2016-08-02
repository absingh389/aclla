"""
BSParser


Author
José Lopes de Oliveira Jr. <bierminen.com>


Overview
BSParser is an Aclla submodule to parse BeerSmith's XML files.  This tool can
help users to build their own databases.

"""


import xml.etree.ElementTree as ET


class Grain(object):
    """
    Retrive data from a bsmx file with grain information --usually Grain.bsmx.

    ARGS:
    - path (string): path to the bsmx file.

    """
    def __init__(self, path):
        self.root = ET.parse(path).getroot()

    def parse(self, tags):
        """
        ARGS:
        - tags (list): a list of tags you want to retrive --see README.md for a
            list of common tags.

        """
        return [dict((tag.tag,tag.text) for tag in el if tag.tag in tags)
            for el in self.root.iter('Grain')]
