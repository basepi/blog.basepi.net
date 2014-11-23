#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Colton Myers'
SITENAME = u'base pi'
SITEURL = ''

# Change to False if there are caching issues
LOAD_CONTENT_CACHE = True

STATIC_PATHS = ['images', 'extra/favicon.png']
EXTRA_PATH_METADATA = {
    'extra/favicon.png': {'path': 'favicon.png'}
}

# chunk theme
THEME = 'themes/pelican-chunk'
SITESUBTITLE = 'because base ten is too boring'
FOOTER_TEXT = 'Powered by <a href="http://getpelican.com">Pelican</a>'
DISPLAY_CATEGORIES_ON_MENU = False
SINGLE_AUTHOR = True
MINT = False
GOOGLE_ANALYTICS = 'UA-56998543-1'

DISQUS_SITENAME = 'blog-basepi-net'

YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_DATE_FORMAT = '%b %d %Y'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
        ('RSS', 'http://blog.basepi.net/rss.xml'),
        ('Github', 'http://github.com/basepi'),
        ('Twitter', 'http://twitter.com/basepi'),
)

TWITTER_USERNAME = 'basepi'

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
