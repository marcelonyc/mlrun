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

import re
import sys
from os import path


sys.path.insert(0, "..")


def current_version():
    root = path.dirname(path.dirname(path.abspath(__file__)))
    with open("{}/mlrun/__init__.py".format(root)) as fp:
        for line in fp:

            # __version__ = '0.4.6'
            match = re.search(r"__version__\s*=\s*'([^']+)'", line)
            if match:
                return match.group(1)
    return "UNKNOWN"


# -- Project information -----------------------------------------------------

project = "mlrun"
copyright = "2020, Iguazio"
author = "Iguazio"

master_doc = "index"

# The short X.Y version
version = current_version()
version = version[: version.rfind(".")]

# The full version, including alpha/beta/rc tags
release = current_version()


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "numpydoc",
    "recommonmark",
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

source_suffix = {
    ".md": "markdown",
    ".rst": "restructuredtext",
}


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"
try:
    import sphinx_rtd_theme  # noqa

    html_theme = "sphinx_rtd_theme"
except ImportError:
    pass

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


def copy_doc(src, dest, title=""):
    """Copy over .md documentation from other parts of the project"""
    with open(dest, "w") as out:
        with open(src) as fp:
            changed = False
            for line in fp:
                if title and re.match("^# .*", line) and not changed:
                    line = f"# {title}"
                    changed = True
                out.write(line)


def setup(app):
    pass


#   project_root = path.dirname(path.dirname(path.abspath(__file__)))
#   copy_doc(f"{project_root}/examples/remote.md", "external/remote.md")
#    copy_doc(
#        f'{project_root}/README.md', 'external/general.md', 'Introduction')
#    copy_doc(
#        f'{project_root}/hack/local/README.md', 'external/install.md')
#    check_call([
#        'jupyter', 'nbconvert',
#        '--output', f'{project_root}/docs/external/basics.html',
#        f'{project_root}/examples/mlrun_basics.ipynb',
#    ])
