import panel as pn

from panel_modal import Modal

pn.extension()

modal = Modal(pn.panel("Hi. I am the Panel Modal!", width=200))

pn.Column(modal.param.open, modal).servable()

