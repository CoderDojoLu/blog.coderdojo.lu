#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'CodeClubLu'
SITENAME = u'CoderDojoLu'
SITEURL = 'https://blog.coderdojo.lu'

PLUGIN_PATHS = ["plugins", "/Users/steve//Desktop/code/pelican-plugins"]
#PLUGINS = ["assets", "liquid_tags", "sitemap", "gravatar", "pdf", "render_math"]
PLUGINS = ["assets", "liquid_tags", "sitemap", "gravatar", "render_math"]

# Make sure to use the zurb-F5-basic theme in THIS directory, it has emoji and video support
THEME = "zurb-F5-basic"

PATH = 'content'

TIMEZONE = 'Europe/Luxembourg'

DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'

TYPOGRIFY = True
DELETE_OUTPUT_DIRECTORY = True
PDF_GENERATOR = True

SITEMAP = {
        'format': 'xml',
        'priorities': {
            'articles': 0.5,
            'indexes': 0.5,
            'pages': 0.5
        },
        'changefreqs': {
            'articles': 'monthly',
            'indexes': 'daily',
            'pages': 'monthly'
        }
    }

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('CodeClubLu', 'http://codeclub.lu/'),
        ('CoderDojo Foundation','http://coderdojo.org'),)

# Social widget

# Use this with standard themes
#SOCIAL = (('CoderDojo on TW', 'https://twitter.com/CoderDojoLu'),
#         ('CoderDojo on FB','https://www.facebook.com/pages/CoderDojo-Luxembourg/1494650000781128'),
#         ('CodeClubLu on TW','https://twitter.com/CodeClubLux'),
#         ('CodeClubLu on FB','https://www.facebook.com/codeclub.lu'),)

# This will add a social icon as an addition
SOCIAL = (('twitter-square', 'https://twitter.com/CoderDojoLu','CoderDojo on TW'),
         ('facebook-square','https://www.facebook.com/pages/CoderDojo-Luxembourg/1494650000781128', 'CoderDojo on FB'),
         ('twitter-square','https://twitter.com/CodeClubLux', 'CodeClub on TW'),
         ('facebook-square','https://www.facebook.com/codeclub.lu', 'CodeClub on FB'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

TWITTER_USERNAME='CoderDojoLu'

DISPLAY_PAGES_ON_MENU = "True"

DEFAULT_CATEGORY = ('welcome')

MD_EXTENSIONS = ['codehilite','extra']
MARKUP = ('md')

COPYRIGHT = 'Public Domain, 2015'
#LOGOTEXT = 'Hack4Kids'
#LOGOIMAGE = '/images/Logo_Hack4Kids_2014_v3.gif'
#PROFILE_IMAGE_URL = '/images/Logo_Hack4Kids_2014_v3.gif'
#COVER_IMG_URL = '/images/cover.png'

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extras/robots.txt': {'path': 'robots.txt'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
    }

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'images',
    'extras/robots.txt',
    'extras/favicon.ico',
    ]
