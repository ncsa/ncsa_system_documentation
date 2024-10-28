# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'NCSA Documentation Hub'
copyright = '2023, University of Illinois'
author = 'University of Illinois'

# RTD recommended config file additions

import os

# Define the canonical URL if you are using a custom domain on Read the Docs
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

# Tell Jinja2 templates the build is running on Read the Docs
if os.environ.get("READTHEDOCS", "") == "True":
    if "html_context" not in globals():
        html_context = {}
    html_context["READTHEDOCS"] = True

# Restoring GitHub link

html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "ncsa", # Username
    "github_repo": "ncsa_system_documentation", # Repo name
    "github_version": os.environ.get("READTHEDOCS_GIT_IDENTIFIER"),  # Version
    "conf_py_path": "/docs/source/", # Path in the checkout to the docs root
}

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_tabs.tabs',
    'sphinx_copybutton',
    'sphinx_design',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'


html_css_files = [
    'css/custom.css',
    'css/tablefix.css',
]

# -- custom JS
html_js_files = [
    'js/custom.js',
]

# -- Logo 
html_static_path = ['_static', 'documents']
html_logo = "images/BlockI-NCSA-Full-Color-RGB_border4.png"
html_theme_options = {
     'logo_only': False,
     'display_version': False,
     'flyout_display': 'attached',
 }

# -- Change page title
html_title = 'UIUC NCSA User Documentation'
