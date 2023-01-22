"""This package provides a Panel Modal that works both on the server and in the notebook.

..code-block::

    import panel as pn
    from panel_modal import Modal

    pn.extension()

    modal = Modal(pn.panel("Hi. I am the Panel Modal!", width=200))

    pn.Column(modal.param.open, modal).servable()
"""
from .modal import Modal

VERSION = "0.2.0"

__all__ = ["Modal", "VERSION"]
