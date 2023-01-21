"""# The Panel `Modal` works on both the server and in the notebook

```bash
pip install panel-modal
```

```python
import panel as pn

from panel_modal import Modal

pn.extension()

modal = Modal(object=pn.panel("Hi. I am the Panel Modal!", width=200))

pn.Column(modal.param.open, modal).servable()
```
"""
import panel as pn
import hvplot.pandas  # noqa
import pandas as pd

from panel_modal import Modal

pn.extension(sizing_mode="stretch_width")

age_list = [8, 10, 12, 14, 72, 74, 76, 78, 20, 25, 30, 35, 60, 85]
df = pd.DataFrame({"gender": list("MMMMMMMMFFFFFF"), "age": age_list})
plot = df.hvplot.box(y='age', by='gender', height=400, width=400, legend=False, ylim=(0, None))

modal_object = pn.Column(
    "## Hi. I'm a *modal*", plot, sizing_mode="fixed", width=600
)
modal = Modal(object=modal_object)

layout = pn.Column(modal.param.open, modal, modal.param.is_open, modal.param.show_close_button)

pn.template.FastListTemplate(
    site="Awesome Panel",
    title="Panel Modal",
    favicon="https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel-assets/320297ccb92773da099f6b97d267cc0433b67c23/favicon/ap-1f77b4.ico",
    main=[__doc__, layout], sizing_mode="stretch_both",
).servable()