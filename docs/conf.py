# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "ART101"
copyright = "2025-2026, Amith Kamath"
# Keep the copyright attribution below, but omit the theme's redundant "By ..." footer line.
author = ""

release = "0.1"
version = "0.1.0"

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx_book_theme",
    "myst_parser",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

master_doc = "index"
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

myst_enable_extensions = ["dollarmath"]
myst_heading_anchors = 3

# -- Options for HTML output

html_theme = "sphinx_book_theme"

html_theme_options = {
    "navigation_depth": 4,  # Depth of nested TOC items
    "show_nav_level": 2,  # Show top-level items expanded
    "collapse_navigation": True,  # Collapse subsections by default
    "extra_footer": (
        '<p>This work is licensed under '
        '<a href="https://creativecommons.org/licenses/by-nc-nd/4.0/" '
        'target="_blank" rel="license noopener noreferrer">'
        'CC BY-NC-ND 4.0</a> '
        '(Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 '
        'International).</p>'
    ),
}

# -- Options for EPUB output
epub_show_urls = "footnote"
