
def test_workchain():
    from aiida.orm import Str
    from aiidalab_qe_hello_world import WorkChain
    from aiida.engine import run_get_node
    name = Str("Xing")
    inputs = {"name": name}
    outputs, node = run_get_node(WorkChain, **inputs)
    assert outputs["name"].value == "Xing"
