from aiidalab_qe_hello_world.setting import Setting
from aiidalab_qe_hello_world.workchain import workchain_and_builder
from aiidalab_qe_hello_world.result import Result
from aiidalab_qe.panel import OutlinePanel

class Outline(OutlinePanel):
    title = "Hello World"
    description = "A aiidalab-qe plugin to print hello world."


property ={
"outline": Outline,
"setting": Setting,
"workchain": workchain_and_builder,
"result": Result,
}
