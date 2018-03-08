#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Al Krinker'
SITENAME = 'Cloud. Big Data. Analytics... and so on'
SITEURL = ''
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Paths
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']
STATIC_PATHS = ['extra', 'notebooks', 'code']
PLUGIN_PATHS = ['pelican-plugins']
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
    'extra/jupyter.css': {'path': 'static/css/jupyter.css'},
    'extra/custom.js': {'path': 'static/js/custom.js'}
}
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

SUMMARY_MAX_LENGTH = 50


# Theme, environements and plugins
THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
# FAVICON = 'extra/favicon.ico'
# AVATAR ='extra/gear-wrench-icon-512-278694.png'
CUSTOM_CSS = 'static/css/custom.css'
CUSTOM_JS = 'static/js/custom.js'
PYGMENTS_STYLE = 'native'

# to ignore any injected css for ipynb pages
IPYNB_IGNORE_CSS = True  ###change back!!!!!!!!!!!!!
# EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')


JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGINS = [
    'i18n_subsites',
    'series',
    'tag_cloud',
    'liquid_tags.img',
    'liquid_tags.youtube',
    'liquid_tags.notebook',
    'liquid_tags.include_code',
    'pelican_javascript',
    'related_posts',
    'render_math',
    'pelican-ipynb.markup',
    'neighbors',
    'tipue_search']


I18N_TEMPLATES_LANG = 'en'

MARKUP = ('md', 'ipynb','html')
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
	    'markdown.extensions.tables': {},
        },
    'output_format': 'html5',
}


# Ignore all files that start with a dot .
IGNORE_FILES = ['.*', '*-checkpoint.ipynb', '.ipynb_checkpoints', '*backup']


# Breadcrumbs
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True


SERIES_TEXT = 'Article %(index)s of the %(name)s series'


# sidebar options
   #  Tag Cloud Options
DISPLAY_SERIES_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
TAG_CLOUD_MAX_ITEMS = 10
   #  Recent Posts in Sidebas
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
RECENT_POST_COUNT = 3
   #  Series infor on sidebar
SHOW_SERIES = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
    # Github on sidebar
GITHUB_USER = 'krinkere'
GITHUB_REPO_COUNT = 5
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True


# Top menus
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True


ARCHIVES_SAVE_AS = 'archives.html'
DISPLAY_ARCHIVE_ON_MENU = True
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'


ABOUT_ME = 'I work as a Data Scientist at USPTO. ' \
           'I am a husband and a father. ' \
           'In my free time, I practice Brazilian Jiu Jitsu. I was awarded Brown belt in December of 2017 by Tony Passos (3rd degree black belt under Ricardo De La Riva)'


# for Tique Search Plugin
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'authors', 'archives', 'search')


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# # Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)
#
# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 5
