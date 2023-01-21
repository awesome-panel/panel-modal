# ✨ panel-modal

We want to make it easy to use *modals* with Panel on both the server and in the notebook.

A *modal* is an element that displays in front of and deactivates all other page content. Panel
already includes a modal. But it only works if you using a *template* on a server. It does not
work in the notebook.

You can install and use the package as simple as.

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

![Panel Modal in Notebook](assets/images/panel-modal.jpg)

Check out the [api](#api) section below and the [examples](apps) folder for more details.

![Project Intro](assets/videos/panel-modal-intro.gif)

## Api

### Parameters

- `object` : The object to display in the modal. You can display multiple objects by wrapping them in
a layout like a Column.
- `is_open`: Whether or not the modal is open. Set this to `True` to open the modal.
- `show_close_button`: Whether to show a close button in the modal.
- `style`: The css styles applied to the modal.

### Events

- `open`: Trigger this to open the modal.
- `close`: Trigger this to close the modal.

## 🚀 Get started in under a minute

Install `panel-modal` including the *`examples` dependencies*.

```bash
pip install  panel-modal[examples]
```

Explore the sample apps

```bash
pn hello panel-modal
```

You can now find the *reference* and *gallery* notebooks in the `examples/awesome-panel/panel-modal` folder. Check them out by running `jupyter lab`.

## 📒 Explore the examples online

Click one of the buttons

[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/awesome-panel/panel-modal/tree/main/examples/)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/awesome-panel/panel-modal/HEAD)

## ⭐ Support

Please support [Panel](https://panel.holoviz.org) and
[awesome-panel](https://awesome-panel.org) by giving the projects a star on Github:

- [holoviz/panel](https://github.com/holoviz/panel).
- [awesome-panel/awesome-panel](https://github.com/awesome-panel/awesome-panel).

Thanks

## ❤️ Contribute

If you are looking to contribute to this project you can find ideas in the [issue tracker](https://github.com/awesome-panel/panel-modal/issues). To get started check out the [DEVELOPER_GUIDE](DEVELOPER_GUIDE.md).

I would love to support and receive your contributions. Thanks.

[![Hacktober Fest](https://github.blog/wp-content/uploads/2022/10/hacktoberfestbanner.jpeg?fit=1200%2C630)](https://github.com/awesome-panel/panel-modal/issues).

## Monitor

[![PyPI version](https://badge.fury.io/py/panel-modal.svg)](https://pypi.org/project/panel-modal/)
[![Downloads](https://pepy.tech/badge/panel-modal/month)](https://pepy.tech/project/panel-modal)
![Python Versions](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue)
[![License](https://img.shields.io/badge/License-MIT%202.0-blue.svg)](https://opensource.org/licenses/MIT)
![Test Results](https://github.com/awesome-panel/panel-modal/actions/workflows/tests.yaml/badge.svg?branch=main)
