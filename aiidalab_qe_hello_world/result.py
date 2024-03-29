from aiidalab_qe.common.panel import ResultPanel
import ipywidgets as ipw


class Result(ResultPanel):
    title = "Hello world"
    workchain_labels = ["hello_world"]

    def _update_view(self):
        name = self.outputs.hello_world.name.value
        formula = self.outputs.hello_world.structure.get_formula()
        self.summary_view = ipw.HTML(
            f"""<div> <h4>Hello {name}</h4> The input structure is: {formula} </div>""".format()
        )
        self.children = [ipw.HBox(children=[self.summary_view])]
