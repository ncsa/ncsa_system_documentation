# Configuration file for the Sphinx documentation builder.
import os

# Set canonical URL from the Read the Docs Domain
# (from Craig: we may need to hard-code the URL as the second argument here, for it to fall back to, in case it's not properly defined in the virtual OS for the build)
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

# Tell Jinja2 templates the build is running on Read the Docs
if os.environ.get("READTHEDOCS", "") == "True":
    html_context["READTHEDOCS"] = True

# -- Project information

project = 'NCSA Documentation Hub'
copyright = '2023, University of Illinois'
author = 'University of Illinois'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_tabs.tabs',
    'sphinx_copybutton',
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
 }

# -- Change page title
html_title = 'UIUC NCSA User Documentation'
