from aiidalab_qe.common.panel import Panel
import ipywidgets as ipw

class Setting(Panel):
    title = "Hello world"
    identifier = "hello_world"

    def __init__(self, **kwargs):
        self.name = ipw.Text(value="", description="Your name:")
        self.children = [self.name]
        super().__init__(**kwargs)

    def get_panel_value(self):
        """Return a dictionary with the current panel state."""
        return {"name": self.name.value}

    def set_panel_value(self, input_dict):
        """Set the panel state from a dictionary."""
        self.name.value = input_dict.get("name", "")