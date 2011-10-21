#! /usr/bin/env python
'''Main runner class for the Blockworld program'''
from OtherMods import RenderWorld
import sys

if __name__ == '__main__':
    try:
        BLOCK = RenderWorld(sys.argv[1])
    except:
        BLOCK = RenderWorld('keys_and_blocks.xml')