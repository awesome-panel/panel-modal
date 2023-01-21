"""We have a Modal"""
import panel as pn

from panel_modal import Modal


def test_constructor():
    """We can construct and work with the Modal"""
    modal = Modal(object=pn.panel("Hi. I am the Panel Modal!", width=200))
    modal.param.trigger("open")
    modal.is_open = True
    modal.param.trigger("close")
    modal.is_open = False
