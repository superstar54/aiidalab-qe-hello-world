from aiidalab_qe.panel import Panel
import ipywidgets as ipw
from aiida.orm import Str


class Setting(Panel):
    title = "Hello world"

    def __init__(self, **kwargs):
        self.name = ipw.Text(value="", description="Your name:")
        self.children = [self.name]
        super().__init__(**kwargs)

    def get_panel_value(self):
        return {"name": Str(self.name.value)}

    def load_panel_value(self, input_dict):
        self.name.value = input_dict.get("name", 1)