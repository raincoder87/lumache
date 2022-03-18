# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.append(os.path.join(os.path.abspath(os.pardir)))
sys.path.insert(0, os.path.abspath('../..'))
autodoc_mock_imports = ["_tkinter"]


# -- Project information -----------------------------------------------------

project = 'genGEO'
copyright = '2022, Geothermal Energy and Geofluids, ETH Zurich'
#copyright = '[Geothermal Energy and Geofluids, ETH Zurich](https://geg.ethz.ch)'
author = 'GEG- ETH Zurich'

sphinx_gallery_conf = {
     'examples_dirs': '../examples',   # path to your example scripts
     'gallery_dirs': 'auto_examples',  # path to where to save gallery generated output
}


# The full version, including alpha/beta/rc tags
#release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'myst_parser',
    'sphinx.ext.duration',
    'sphinx.ext.autosectionlabel',
#    'sphinx_gallery.gen_gallery',
#    'nbsphinx',
    'sphinx_thebe'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

html_logo = '../small_logo.jpg'
html_title = 'Documentation'

html_theme_options = {
    "path_to_docs": "docs",
    "repository_url": "https://github.com/GEG-ETHZ/genGEO",
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "colab_url": "https://colab.research.google.com/",
        "deepnote_url": "https://deepnote.com/",
        "notebook_interface": "jupyterlab",
        "thebe": True,
        # "jupyterhub_url": "https://datahub.berkeley.edu",  # For testing
    },
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "use_download_button": True,
    "logo_only": True,
    "show_toc_level": 2,
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# WARNING: `mathjax3_config['options']['processHtmlClass']` is being overridden by 
# myst-parser to tex2jax_process|mathjax_process|math. Set `myst_mathjax_classes = None` 
# if this is undesirable.

#myst_mathjax_classes = None