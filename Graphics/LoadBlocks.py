'''A class containing static methods for loading blockworld xml files'''
__author__ = "Emily and Andrew"
__date__ = "21 October 2011"

from Block import Block
from xml.dom.minidom import parse

class LoadBlocks:
    '''A class containing static methods for loading blockworld xml files'''

    @staticmethod
    def load(f_name):
        '''Call this static method to load a list of blocks from an xml file (f_name). Returns a list of Blocks.'''
        block_list = []
        dom1 = parse(f_name)
        blocks = dom1.getElementsByTagName('BLOCK')
        for block in blocks:
            block_list.append(LoadBlocks.add_block(block))
        return block_list

    @staticmethod
    def add_block(top_node):
        '''Method called for each BLOCK tag in the xml document. Adds a Block to the list with the proper attributes.'''
        tags = {}
        for i in top_node.childNodes:
            if i.hasChildNodes():
                tags[i.nodeName] = i.firstChild.nodeValue
        block = Block((tags['X'], tags['Y'], tags['Z']), (tags['RED'], tags['GREEN'], tags['BLUE']))
        return block