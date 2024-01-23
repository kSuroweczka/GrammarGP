from library.Model.node import *
from library.Model.program import Program

def deep_copy_tree(program: Program):
    new_tree = ScopeNode(NodeType.SCOPE, None, [])
    for child in program.ROOT.children_nodes:
        new_tree.children_nodes.append(child)
    # print("NEW_TREE:   ", new_tree)
    return new_tree