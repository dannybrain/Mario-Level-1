#!/usr/bin/env python3
__author__ = 'justinarmstrong'

"""
This is an attempt to recreate the first level of
Super Mario Bros for the NES.
"""

import sys
import pygame as pg
from data.main import main
# this one is unused : import cProfile

if __name__ == '__main__':
    main()
    pg.quit()
    sys.exit()
