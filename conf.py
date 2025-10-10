# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GGW LDM'
copyright = '2025, OSS'
author = 'OSS'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    "repository_url": "https://github.com/kambioss/Documentation_GGW_LDN",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_download_button": True,
    "home_page_in_toc": True,
    "show_toc_level": 2,
}

html_static_path = ['_static']
#html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
import os

if os.environ.get('READTHEDOCS') == 'True':
    html_output_dir = os.path.join(os.environ.get('READTHEDOCS_OUTPUT', '_build'), 'html')
    if not os.path.exists(html_output_dir):
        os.makedirs(html_output_dir)