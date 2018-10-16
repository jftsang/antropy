#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# entropy documentation build configuration file, created by
# sphinx-quickstart on Sun Apr  1 17:42:21 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

import os
import sys
import time
import entropy
import sphinx_bootstrap_theme


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
sys.path.insert(0, os.path.abspath('sphinxext'))
extensions = [
              # 'sphinx.ext.mathjax',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages',
              'sphinx.ext.autosummary',
              'sphinx.ext.autodoc',
              # 'plot_generator',
              # 'plot_directive',
              'numpydoc']

# Generate the API documentation when building
autosummary_generate = True
numpydoc_show_class_members = False

# Include the example source for plots in API docs
plot_include_source = True
plot_formats = [("png", 90)]
plot_html_show_formats = False
plot_html_show_source_link = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'entropy'
author = 'Raphael Vallat'
copyright = u'2018-{}, Raphael Vallat'.format(time.strftime("%Y"))

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# The full version, including alpha/beta/rc tags.
sys.path.insert(0, os.path.abspath(os.path.pardir))
version = entropy.__version__
release = entropy.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# Read the doc theme
# html_theme = "sphinx_rtd_theme"
# html_theme_path = ["_themes", ]
# html_theme_options = {
#     'canonical_url': '',
#     'analytics_id': '',
#     'logo_only': False,
#     'display_version': True,
#     'prev_next_buttons_location': 'bottom',
#     'collapse_navigation': False,
#     'sticky_navigation': True,
#     'navigation_depth': 4,
#     'includehidden': True,
#     'titles_only': False
# }

# Bootstrap theme
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_theme_options = {
    'source_link_position': "footer",
    'bootswatch_theme': "readable",
    'navbar_sidebarrel': False,
    'nosidebar': True,
    'navbar_pagenav': False,
    'bootstrap_version': "3",
    'navbar_links': [
                     ("API", "api"),
                     ("What's new", "changelog")
                     ],

    }

html_logo = 'pictures/entropy_128x128.png'
html_favicon = 'pictures/entropy.ico'

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'entropydoc'
html_static_path = ['_static']
html_show_sourcelink = False
html_add_permalinks = ""


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'entropy.tex', 'entropy Documentation',
     'Raphael Vallat', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'entropy', 'entropy Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'entropy', 'entropy Documentation',
     author, 'entropy', 'Entropy of time-series in Python',
     'Miscellaneous'),
]

# Add the 'copybutton' javascript, to hide/show the prompt in code
# examples, originally taken from scikit-learn's doc/conf.py
def setup(app):
    app.add_javascript('copybutton.js')
    app.add_stylesheet('style.css')