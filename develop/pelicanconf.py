#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys
sys.path.append('.')


LOAD_CONTENT_CACHE = False

AUTHOR = u'PhysicsML'
SITENAME = u'&#12296&nbsp;physics&nbsp;&#124;&nbsp;machine&nbsp;learning&nbsp;&#12297;'
SITEURL = ''

TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'

from utils import filters
JINJA_FILTERS = { 'sidebar': filters.sidebar }

PATH = 'content'

THEME = "themes/custom_fresh"
#THEME = "themes/twenty"
PLUGIN_PATHS=["./plugins"]
PLUGINS = ["render_math.math"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True

MENUITEMS = [("Papers","/papers.html"),]
#DISPLAY_PAGES_ON_MENU = True
#MENUITEMS = [("Papers","/papers.html"),("Sign up!","/signup.html"),]
#TEMPLATE_PAGES = {'papers.html' : 'papers.html' }
#DISPLAY_CATEGORIES_ON_MENU = False

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)
#
## Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
