import os
import sys

sys.path.insert(0, os.path.abspath('../src'))
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SmartMenue'
copyright = '2024, Guillaume BOURGEON, Romain LAUP'
author = 'Guillaume BOURGEON, Romain LAUP'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',       # Pour extraire la documentation des docstrings
    'sphinx.ext.napoleon',      # Support Google et NumPy docstring style
    'recommonmark',             # Pour Markdown si nécessaire
    'sphinx.ext.viewcode',      # Ajoute un lien vers le code source
    'sphinx.ext.todo'           # Support des TODO
]

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


latex_engine = 'pdflatex'
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
}