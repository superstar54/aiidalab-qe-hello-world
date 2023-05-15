from aiidalab_qe.panel import ResultPanel
import ipywidgets as ipw


class Result(ResultPanel):
    title = "Hello world"
    workchain_label = "hello_world"

    def _update_view(self):
        self.summary_view = ipw.HTML(
            """<div> <h4>Hello world: {}</h4> </div>""".format(self.node.outputs.name.value)
        )
        self.children = [ipw.HBox(children=[self.summary_view])]
