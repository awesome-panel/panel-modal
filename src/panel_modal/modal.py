"""A *modal* is an element that displays in front of and deactivates all other page content."""
import param
from panel.reactive import ReactiveHTML

JS_FILE = "https://cdn.jsdelivr.net/npm/a11y-dialog@7/dist/a11y-dialog.min.js"

STYLE = """
.dialog-container,
.dialog-overlay {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}
.dialog-container {
  z-index: 100002;
  display: flex;
}
.dialog-container[aria-hidden='true'] {
  display: none;
}
.dialog-overlay {
  z-index: 100001;
  background-color: rgb(43 46 56 / 0.9);
}
.dialog-content {
  margin: auto;
  z-index: 100002;
  position: relative;
  background-color: white; 
  border-radius: 2px;
  padding: 10px;
  padding-bottom: 20px;
}
fast-design-system-provider .dialog-content {
  background-color: var(--background-color);
  border-radius:  calc(var(--corner-radius) * 1px);
}
@keyframes fade-in {
  from {
    opacity: 0;
  }
}
@keyframes slide-up {
  from {
    transform: translateY(10%);
  }
}
.dialog-overlay {
  animation: fade-in 200ms both;
}
.dialog-content {
  animation: fade-in 400ms 200ms both, slide-up 400ms 200ms both;
}
@media (prefers-reduced-motion: reduce) {
  .dialog-overlay,
  .dialog-content {
    animation: none;
  }
}
.pnx-dialog-close {
  position: absolute;
  top: 0.5em;
  right: 0.5em;
  border: 0;
  padding: 0.25em;
  background-color: transparent;
  font-size: 1.5em;
  width: 1.5em;
  height: 1.5em;
  text-align: center;
  cursor: pointer;
  transition: 0.15s;
  border-radius: 50%;
  z-index: 10003;
}
fast-design-system-provider .pnx-dialog-close {
  color:  var(--neutral-foreground-rest);
}
.pnx-dialog-close:hover {
  background-color: rgb(50 50 0 / 0.15);;
}
fast-design-system-provider .pnx-dialog-close:hover {
  background-color: var(--neutral-fill-hover);
}
.lm-Widget.p-Widget.lm-TabBar.p-TabBar.lm-DockPanel-tabBar.jp-Activity {
  z-index: -1;
}
"""

JS = """
<script async=false defer=false type="application/javascript">
!function(t,e){"object"==typeof exports&&"undefined"!=typeof module?module.exports=e():"function"==typeof define&&define.amd?define(e):(t="undefined"!=typeof globalThis?globalThis:t||self).A11yDialog=e()}(this,(function(){"use strict";var t=['a[href]:not([tabindex^="-"])','area[href]:not([tabindex^="-"])','input:not([type="hidden"]):not([type="radio"]):not([disabled]):not([tabindex^="-"])','input[type="radio"]:not([disabled]):not([tabindex^="-"])','select:not([disabled]):not([tabindex^="-"])','textarea:not([disabled]):not([tabindex^="-"])','button:not([disabled]):not([tabindex^="-"])','iframe:not([tabindex^="-"])','audio[controls]:not([tabindex^="-"])','video[controls]:not([tabindex^="-"])','[contenteditable]:not([tabindex^="-"])','[tabindex]:not([tabindex^="-"])'];function e(t){this._show=this.show.bind(this),this._hide=this.hide.bind(this),this._maintainFocus=this._maintainFocus.bind(this),this._bindKeypress=this._bindKeypress.bind(this),this.$el=t,this.shown=!1,this._id=this.$el.getAttribute("data-a11y-dialog")||this.$el.id,this._previouslyFocused=null,this._listeners={},this.create()}function i(t,e){return i=(e||document).querySelectorAll(t),Array.prototype.slice.call(i);var i}function n(t){(t.querySelector("[autofocus]")||t).focus()}function s(){i("[data-a11y-dialog]").forEach((function(t){new e(t)}))}return e.prototype.create=function(){this.$el.setAttribute("aria-hidden",!0),this.$el.setAttribute("aria-modal",!0),this.$el.setAttribute("tabindex",-1),this.$el.hasAttribute("role")||this.$el.setAttribute("role","dialog"),this._openers=i('[data-a11y-dialog-show="'+this._id+'"]'),this._openers.forEach(function(t){t.addEventListener("click",this._show)}.bind(this));const t=this.$el;return this._closers=i("[data-a11y-dialog-hide]",this.$el).filter((function(e){return e.closest('[aria-modal="true"], [data-a11y-dialog]')===t})).concat(i('[data-a11y-dialog-hide="'+this._id+'"]')),this._closers.forEach(function(t){t.addEventListener("click",this._hide)}.bind(this)),this._fire("create"),this},e.prototype.show=function(t){return this.shown||(this._previouslyFocused=document.activeElement,this.$el.removeAttribute("aria-hidden"),this.shown=!0,n(this.$el),document.body.addEventListener("focus",this._maintainFocus,!0),document.addEventListener("keydown",this._bindKeypress),this._fire("show",t)),this},e.prototype.hide=function(t){return this.shown?(this.shown=!1,this.$el.setAttribute("aria-hidden","true"),this._previouslyFocused&&this._previouslyFocused.focus&&this._previouslyFocused.focus(),document.body.removeEventListener("focus",this._maintainFocus,!0),document.removeEventListener("keydown",this._bindKeypress),this._fire("hide",t),this):this},e.prototype.destroy=function(){return this.hide(),this._openers.forEach(function(t){t.removeEventListener("click",this._show)}.bind(this)),this._closers.forEach(function(t){t.removeEventListener("click",this._hide)}.bind(this)),this._fire("destroy"),this._listeners={},this},e.prototype.on=function(t,e){return void 0===this._listeners[t]&&(this._listeners[t]=[]),this._listeners[t].push(e),this},e.prototype.off=function(t,e){var i=(this._listeners[t]||[]).indexOf(e);return i>-1&&this._listeners[t].splice(i,1),this},e.prototype._fire=function(t,e){var i=this._listeners[t]||[],n=new CustomEvent(t,{detail:e});this.$el.dispatchEvent(n),i.forEach(function(t){t(this.$el,e)}.bind(this))},e.prototype._bindKeypress=function(e){const n=document.activeElement;n&&n.closest('[aria-modal="true"]')!==this.$el||(this.shown&&"Escape"===e.key&&"alertdialog"!==this.$el.getAttribute("role")&&(e.preventDefault(),this.hide(e)),this.shown&&"Tab"===e.key&&function(e,n){var s=function(e){return i(t.join(","),e).filter((function(t){return!!(t.offsetWidth||t.offsetHeight||t.getClientRects().length)}))}(e),o=s.indexOf(document.activeElement);n.shiftKey&&0===o?(s[s.length-1].focus(),n.preventDefault()):n.shiftKey||o!==s.length-1||(s[0].focus(),n.preventDefault())}(this.$el,e))},e.prototype._maintainFocus=function(t){!this.shown||t.target.closest('[aria-modal="true"]')||t.target.closest("[data-a11y-dialog-ignore-focus-trap]")||n(this.$el)},"undefined"!=typeof document&&("loading"===document.readyState?document.addEventListener("DOMContentLoaded",s):window.requestAnimationFrame?window.requestAnimationFrame(s):window.setTimeout(s,16)),e}));
</script>
"""


class Modal(ReactiveHTML):  # pylint: disable=too-many-ancestors
    """A *modal* is an element that displays in front of and deactivates all other page content.

    You will need to include the Modal in your layout or template. It will not be shown before
    you `open` it.

    Args:
        object: The object to display in the modal. You can display multiple objects by
        wrapping them in a layout like a Column.

    Example:

    ..code-block:

        import panel as pn
        from panel_modal import Modal

        pn.extension()

        modal = Modal(object=pn.panel("Hi. I am the Panel Modal!", width=200))

        pn.Column(modal.param.open, modal).servable()
    """

    object = param.Parameter(
        doc="""The object to display in the modal.
    You can display multiple objects by wrapping them in a layout like a Column."""
    )

    open = param.Event(doc="Trigger this to open the modal.")
    close = param.Event(doc="Trigger this to close the modal.")
    is_open = param.Boolean(doc="Whether or not the modal is open.")
    show_close_button = param.Boolean(True, doc="Whether to show a close button in the modal")

    style = param.String(STYLE, doc="The css styles applied to the modal")

    def __init__(self, object, **params):  # pylint: disable=redefined-builtin
        super().__init__(object=object, height=0, width=0, margin=0, **params)

    @param.depends("open", watch=True)
    def _show(self):
        self.is_open = True

    @param.depends("close", watch=True)
    def _hide(self):
        self.is_open = False

    __javascript__ = [JS_FILE]

    _template = """
<style id="pnx_dialog_style">
{{style}}
</style>
<div id="pnx_dialog" class="dialog-container bk-root" aria-hidden="true">
<div class="dialog-overlay" data-a11y-dialog-hide></div>
  <div id="pnx_dialog_content" class="dialog-content" role="document">
    <button id="pnx_dialog_close" data-a11y-dialog-hide class="pnx-dialog-close" aria-label="Close this dialog window">
      <svg class="svg-icon" viewBox="0 0 20 20">
        <path
          fill="currentcolor"
          d="M15.898,4.045c-0.271-0.272-0.713-0.272-0.986,0l-4.71,4.711L5.493,4.045c-0.272-0.272-0.714-0.272-0.986,0s-0.272,0.714,0,0.986l4.709,4.711l-4.71,4.711c-0.272,0.271-0.272,0.713,0,0.986c0.136,0.136,0.314,0.203,0.492,0.203c0.179,0,0.357-0.067,0.493-0.203l4.711-4.711l4.71,4.711c0.137,0.136,0.314,0.203,0.494,0.203c0.178,0,0.355-0.067,0.492-0.203c0.273-0.273,0.273-0.715,0-0.986l-4.711-4.711l4.711-4.711C16.172,4.759,16.172,4.317,15.898,4.045z"
        ></path>
      </svg>
    </button>
    ${object}
  </div>
</div>
"""

    _scripts = {
        "render": """
        fast_el = document.getElementById("body-design-provider")
        if (fast_el!==null){
          fast_el.appendChild(pnx_dialog)
        }
        self.show_close_button()
        self.init_modal()
        """,
        "init_modal": """
state.modal = new A11yDialog(pnx_dialog)
state.modal.on('show', function (element, event) {data.is_open=true})
state.modal.on('hide', function (element, event) {data.is_open=false})
""",
        "is_open": "if (data.is_open==true){state.modal.show()} else {state.modal.hide()}",
        "show_close_button": """
if (data.show_close_button){pnx_dialog_close.style.display = " block"}else{pnx_dialog_close.style.display = "none"}
""",
    }


def _handle_notebook():
    """In Notebook special care is needed"""
    try:
        # Imports the A11 Modal js in the notebook
        display  # pylint: disable=pointless-statement
        from IPython.core.display import HTML  # pylint: disable=import-outside-toplevel

        display(HTML(JS))

        # Handles case wher user restarts kernel and runs all
        Modal._scripts[  # pylint: disable=protected-access
            "init_modal"
        ] = """
pnx = pnx_dialog
dt = data
setTimeout(function(){
    state.modal = new A11yDialog(pnx)
    state.modal.on('show', function (element, event) {dt.is_open=true})
    state.modal.on('hide', function (element, event) {dt.is_open=false})   
}, 100);
"""
    except NameError:
        pass


_handle_notebook()
