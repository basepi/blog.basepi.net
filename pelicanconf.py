#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Colton Myers'
SITENAME = u'base pi'
SITEURL = ''

LOAD_CONTENT_CACHE = False

# chunk theme
SITESUBTITLE = 'because base ten is too boring'
FOOTER_TEXT = 'Powered by <a href="http://getpelican.com">Pelican</a>'
DISPLAY_CATEGORIES_ON_MENU = True
SINGLE_AUTHOR = True
MINT = False
GOOGLE_ANALYTICS = 'UA-56998543-1'

THEME = 'themes/pelican-chunk'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_DATE_FORMAT = '%b %d %Y'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
