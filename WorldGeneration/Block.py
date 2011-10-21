'''Stores information about a certain block'''
__author__ = "Emily and Andrew"
__date__ = "21 October 2011"
from ObjectPosition import ObjectPosition
from ObjectColor import ObjectColor
from WorldObject import WorldObject

class Block(WorldObject):
    '''Stores information about an object, including its position in space and its color'''

    def __init__(self, position, color):
        '''Initializes the key's color and position. Takes two 3-tuples (xyz and rgb)'''

        #super(Block, self).__init__(self, position, color)        #format from lecture
        WorldObject.__init__(self, position, color)                #format from ibiblio website


        
    def get_type(self):
        return "block"
