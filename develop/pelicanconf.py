#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys
sys.path.append('.')


LOAD_CONTENT_CACHE = False

AUTHOR = u'PhysicsML'
SITENAME = u'&#12296&nbsp;physics&nbsp;&#124;&nbsp;machine&nbsp;learning&nbsp;&#12297;'
SITEURL = 'https://physicsml.github.io'

TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'

from utils import filters
JINJA_FILTERS = { 'sidebar': filters.sidebar }

PATH = 'content'

#THEME = "themes/custom_fresh"
THEME = "themes/twenty"
PLUGIN_PATHS=["./plugins"]
PLUGINS = ["render_math.math"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)
#
## Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 3
POST_LIMIT = 3

# Show most recent posts first
NEWEST_FIRST_ARCHIVES = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#MENUITEMS = [("News", "/category/news.html"), ("Blog", "/category/articles.html"), ("Papers", "/pages/papers.html")]
MENUITEMS = [("News", "/news.html"), ("Blog", "/articles.html"), ("Papers", "/papers.html")]

#TEMPLATE_PAGES = {'/themes/twenty/templates/page.html' : 'papers.html' }

# Formatting for urls
ARTICLE_PATHS = ['Articles', 'News']
ARTICLE_URL = "blog/{slug}.html"
ARTICLE_SAVE_AS = "blog/{slug}.html"

#ARCHIVES_URL = "blog"
#ARCHIVES_SAVE_AS = "blog/index.html"

PAGE_PATHS = ['Pages']
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

#CATEGORY_URL = "category/{slug}/"
#CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}.html"

USE_FOLDER_AS_CATEGORY = False #True


#DISPLAY_PAGES_ON_MENU = True
#DISPLAY_CATEGORIES_ON_MENU = True

# Generate yearly archive
#YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'

# Formatting for dates
DEFAULT_DATE_FORMAT = ('%d-%m-%Y')

STATIC_PATHS = ['images',
                'fonts',
                'css',
                'js',
                ]

import datetime
now = datetime.datetime.utcnow()
YEAR = now.strftime("%Y")
