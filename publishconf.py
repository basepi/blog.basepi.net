#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

#sys.path.append(os.curdir)
# This is the directory where your pelican's
# configuration files reside
pelicanpath = '/home/basepi/Dropbox/Blogs/blog.basepi.net'
sys.path.append(pelicanpath)

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://blog.basepi.net'
RELATIVE_URLS = False

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
