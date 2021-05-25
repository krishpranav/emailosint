#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports
import sys
import json
from lib.color import *
from recon.pwned import *
from recon.shodan import *

def plus(string):print("%s[+]%s %s"%(G%0,E,string))
def warn(string):print("%s[!]%s %s"%(R%0,E,string))
def test(string):print("%s[*]%s %s"%(B%0,E,string))
def info(string):print("%s[i]%s %s"%(Y%0,E,string))
def more(string):print(" %s|%s  %s"%(W%0,E,string))