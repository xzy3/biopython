#!/usr/bin/env python3
"""Biopython Sphinx documentation build configuration file.

After generating ``*.rst`` files from the source code, this
file controls running ``sphinx-build`` to turn these into
human readable documentation.
"""

import os
import shutil
import sys
import tempfile

from sphinx.ext import autodoc

from Bio import __version__, Application

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = "4.3.2"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    # Don't want to include source code in the API docs
    # 'sphinx.ext.viewcode',
    "sphinx.ext.autosummary",
    "numpydoc",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Biopython"
copyright = "1999-2024, The Biopython Contributors"
author = "The Biopython Contributors"
document = "Biopython API Documentation"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = __version__  # TODO: Shorten this
# The full version, including alpha/beta/rc tags.
release = __version__

# Versions for versions.html:
# (this will break if we have version gaps)
try:
    main_version, minor_version, _ = version.split(".")  # e.g. 1.79.dev0
    dev_version = True
except ValueError:
    main_version, minor_version = version.split(".")  # e.g. 1.78
    dev_version = False
prev_minor_version = int(minor_version) - (2 if dev_version else 1)
previous_version = f"{main_version}.{prev_minor_version}"
versions = [
    ("Previous", f"../{previous_version}/"),
    ("Latest", "../latest/"),
    ("Develop", "../dev/"),
]

if version < "1.75":  # 1.74 is the earliest Sphinx-generated api documentation
    del versions[0]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README.rst", "doc.rst"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# If true, figures, tables and code-blocks are automatically numbered if
# they have a caption. The numref role is enabled.
numfig = True

# -- Options for autodoc --------------------------------------------------

# This requires Sphinx 1.8 or later:
autodoc_default_options = {
    "members": None,
    "undoc-members": None,
    "special-members": None,
    "show-inheritance": None,
    "member-order": "bysource",
    "exclude-members": "__dict__,__weakref__,__module__",
}

# Experimental feature to preserve the default argument values of
# functions in source code and keep them not evaluated for readability:
autodoc_preserve_defaults = True

# To avoid import errors.
autodoc_mock_imports = ["MySQLdb"]

# -- Options for HTML output ----------------------------------------------

# Sphinx default was html_theme = "alabaster"
html_theme = "sphinx_rtd_theme"

# Sphinx Read The Docs theme settings, see
# https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html
html_theme_options = {
    "prev_next_buttons_location": "both",
    # Same a Hyde theme sidebar on biopython.org:
    "style_nav_header_background": "#10100F",
    # Since we have the Biopython logo via html_logo,
    "logo_only": True,
}

# Based on:
# https://github.com/readthedocs/sphinx_rtd_theme/issues/231#issuecomment-126447493
html_context = {
    "display_github": True,  # Add 'Edit on Github' link instead of 'View page source'
    "github_user": "biopython",
    "github_repo": "biopython",
    "github_version": "master",
    "conf_py_path": "/Doc/",
    # "source_suffix": source_suffix,
    "theme_display_version": False,
    # Biopython-specific values for version-footer (versions.html):
    "display_version_footer": True,
    "current_version": version,
    "versions": versions,
    "project_home_url": "https://biopython.org",
    "project_github_url": "https://github.com/biopython/biopython",
}

html_logo = "images/biopython_logo.svg"

# The RST source is transient, don't need/want to include it
html_show_sourcelink = False
html_copy_source = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# The following is not applicable to the Read-the-docs theme:
# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
# html_sidebars = {
#     "**": [
#         "about.html",
#         "navigation.html",
#         "relations.html",  # needs 'show_related': True theme option to display
#         "searchbox.html",
#         "donate.html",
#     ]
# }


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "Biopython_doc"


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
    (master_doc, "Biopython_doc.tex", document, author, "manual"),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "biopython", document, [author], 1)]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "Biopython",
        document,
        author,
        "Biopython",
        "Collection of modules for dealing with biological data in Python.",
        "Miscellaneous",
    )
]


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = document  # project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]

# -- Options for numpydoc -------------------------------------------------

numpydoc_class_members_toctree = False
# Prevents the attributes and methods from being shown twice
numpydoc_show_class_members = False

# -- Magic to run sphinx-apidoc automatically -----------------------------

# See https://github.com/rtfd/readthedocs.org/issues/1139
# on which this is based.


def insert_github_link(filename):
    """Insert file specific :github_url: metadata for theme breadcrumbs."""
    assert "/" not in filename and filename.endswith(".rst")
    with open(filename) as handle:
        text = handle.read()
    if ":github_url:" in text:
        return

    python = filename[:-4].replace(".", "/") + "/__init__.py"
    if not os.path.isfile(os.path.join("../../", python)):
        python = filename[:-4].replace(".", "/") + ".py"
    if not os.path.isfile(os.path.join("../../", python)):
        sys.stderr.write(
            "WARNING: Could not map %s to a Python file, e.g. %s\n" % (filename, python)
        )
        return

    text = ":github_url: https://github.com/%s/%s/blob/%s/%s\n\n%s" % (
        html_context["github_user"],
        html_context["github_repo"],
        html_context["github_version"],
        python,
        text,
    )
    with open(filename, "w") as handle:
        handle.write(text)


def run_apidoc(_):
    """Call sphinx-apidoc on Bio and BioSQL modules."""
    from sphinx.ext.apidoc import main as apidoc_main

    cur_dir = os.path.abspath(os.path.dirname(__file__))
    # Can't see a better way than running apidoc twice, for Bio & BioSQL
    # We don't care about the index.rst / conf.py (we have our own)
    # or the Makefile / make.bat (effectively same) clashing,
    # $ sphinx-apidoc -e -F -o /tmp/api/BioSQL BioSQL
    # $ sphinx-apidoc -e -F -o /tmp/api/Bio Bio
    tmp_path = tempfile.mkdtemp()
    apidoc_main(["-e", "-F", "-o", tmp_path, "../BioSQL"])
    apidoc_main(
        [
            "-e",
            "-F",
            "-o",
            tmp_path,
            # The input path:
            "../Bio",
            # These are patterns to exclude:
            "../Bio/Alphabet/",
            "../Bio/Restriction/Restriction.py",
        ]
    )
    os.remove(os.path.join(tmp_path, "index.rst"))  # Using our own
    for filename in os.listdir(tmp_path):
        if filename.endswith(".rst"):
            shutil.move(
                os.path.join(tmp_path, filename), os.path.join(cur_dir, "api", filename)
            )
    shutil.rmtree(tmp_path)

    for f in os.listdir(cur_dir):
        if f.startswith("Bio") and f.endswith(".rst"):
            insert_github_link(f)


class BioPythonAPI(autodoc.ClassDocumenter):
    """Custom Class Documenter for AbstractCommandline classes."""

    def import_object(self):
        """Import the class."""
        ret = super().import_object()

        if not issubclass(self.object, Application.AbstractCommandline):
            return ret

        try:
            # If the object is an AbstractCommandline we instantiate it.
            self.object()
        except TypeError:
            # Throws if the object is the base AbstractCommandline class
            pass
        return ret


def setup(app):
    """Over-ride Sphinx setup to trigger sphinx-apidoc."""
    app.connect("builder-inited", run_apidoc)

    app.add_css_file("biopython.css")

    def add_documenter(app, env, docnames):
        app.add_autodocumenter(BioPythonAPI, True)

    # Over-ride autodoc documenter
    app.connect("env-before-read-docs", add_documenter)
