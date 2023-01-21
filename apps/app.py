"""# Awesome Panel Starter Project

This project was created with the [awesome-panel-cli](https://github.com/awesome-panel/awesome-panel-cli)
"""
import panel as pn

pn.extension(sizing_mode="stretch_width")

pn.template.FastListTemplate(
    site="Awesome Panel",
    title="Starter App",
    favicon="https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel-assets/320297ccb92773da099f6b97d267cc0433b67c23/favicon/ap-1f77b4.ico",
    main=[__doc__], sizing_mode="stretch_both",
).servable()