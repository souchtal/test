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
import os, subprocess
import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'docu'
copyright = '2020, saw'
author = 'saw'
# The full version, including alpha/beta/rc tags
release = '1.2'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#sys.path.append( "/home/bscuser/Documents/breathe/test/docs/source" )
#extensions = ['sphinx.ext.pngmath', 'sphinx.ext.todo', 'breathe' ]
extensions = [ 'breathe' ]
#use relative path
#breathe_projects= {"docu": "/home/bscuser/Documents/breathe/test/doc/Doxygen/xml"}
breathe_projects= {"docu": "../../doc/Doxygen/xml"}
breathe_default_project = "docu"


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
import sphinx_rtd_theme


html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# def setup(app):
#     app.add_stylesheet("main_stylesheet.css")

html_logo  = '_static/fti_pic.jpeg'
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']  

#added code 
# def configureDoxyfile(input_dir, output_dir):
#     with open('Doxyfile', 'r') as file :
#         filedata = file.read()
 
#     filedata = filedata.replace('@DOXYGEN_INPUT_DIR@', input_dir)
#     filedata = filedata.replace('@DOXYGEN_OUTPUT_DIR@', output_dir)
 
#     with open('Doxyfile', 'w') as file:
#         file.write(filedata)
 
# # Check if we're running on Read the Docs' servers
read_the_docs_build = os.environ.get('READTHEDOCS', None) == 'True'
 
# breathe_projects = {}
 
if read_the_docs_build:
	subprocess.call('cd ../../doc/Doxygen; doxygen Doxyfile', shell=True)
#     input_dir = '../CatCutifier'
#     output_dir = 'build'
#     configureDoxyfile(input_dir, output_dir)
#     subprocess.call('doxygen', shell=True)
#     breathe_projects['CatCutifier'] = output_dir + '/xml'
