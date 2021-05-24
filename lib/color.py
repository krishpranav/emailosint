#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# color file this file contains all the color for the whole tool

# imports
import sys
import colorama

if sys.platform == 'win32':
    colorama.init()

# colors
R = "\033[%s;31m"
B = "\033[%s;34m"
G = "\033[%s;32m"
W = "\033[%s;38m"
Y = "\033[%s;33m"
E = "\033[0m"

