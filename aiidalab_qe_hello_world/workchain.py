
from aiidalab_qe.panel import PropertyPanel, ResultPanel, Panel
from aiida.engine import ToContext, WorkChain, calcfunction
from aiida.orm import Str, Dict, StructureData


class HelloWorldWorkChain(WorkChain):
    identifier = "hello_world"
    """WorkChain to print hello world."""

    @classmethod
    def define(cls, spec):
        """Specify inputs and outputs."""
        super().define(spec)
        spec.input('structure', valid_type=StructureData)
        spec.input('name', valid_type=Str)
        spec.outline(
            cls.result,
        )
        spec.output('name', valid_type=Str)

    @classmethod
    def get_builder_from_protocol(cls, codes=None, structure=None, parameters=None):
        builder = cls.get_builder()
        builder.name = parameters["name"]
        builder.structure = structure
        return builder

    def result(self):
        """Add the result to the outputs."""
        self.out("name", self.inputs.name)

def get_builder(codes, structure, parameters):
    """Get the workchain specific parameters
    """
    parameters = parameters.get("hello_world", {})
    builder = HelloWorldWorkChain.get_builder_from_protocol(
                codes=codes,
                structure=structure,
                parameters=parameters,
            )
    return builder
    

subworkchain = [HelloWorldWorkChain, get_builder]