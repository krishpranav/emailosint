#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports

from lib.output import *
try:
    from urllib.parse import urlparse
except ImportError as e:
    from urlparse import urlparse

def checkTarget(target):
    o = urlparse(target)
    if o.netloc == "":
        if "www." in o.path: return o.path.split('www.')[1]
        return o.path
    elif o.netloc != "":
        if "www." in o.netloc: return o.netloc.split("www.")[1]
        return o.netloc
    else: return target

def checkEmail(email):
    if '@' not in email:
        exit(warn('Invalid email %s'%email))
    return email

