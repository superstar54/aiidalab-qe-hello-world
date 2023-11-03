
from aiida.engine import WorkChain
from aiida.orm import Str, StructureData


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
        spec.output('structure', valid_type=StructureData)

    @classmethod
    def get_builder_from_protocol(cls, codes=None, structure=None, parameters=None):
        builder = cls.get_builder()
        builder.name = Str(parameters["name"])
        builder.structure = structure
        return builder

    def result(self):
        """Add the result to the outputs."""
        self.out("name", self.inputs.name)
        self.out("structure", self.inputs.structure)

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


workchain_and_builder = {
        "workchain": HelloWorldWorkChain,
        "get_builder": get_builder,
        }