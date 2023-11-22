from library.Model.program import Program
from library.Model.node import *

# TO DO?
# def runProgram(program: Program) -> Program:
#     parsed_program = parsProgram(program)
#     print(parsed_program)
#     new_program = Program(program.task, program.max_depth, program.min_rand, program.max_rand)
#     index = 0

#     def walk(parsed_program, new_program, node):
#         if index == len(parsed_program):
#             return
#         index += 1
#         if node == 'INPUT':
#             new_program.ROOT.add_child(new_program.createNode(NodeType.INPUT, new_program.ROOT))
#             walk(parsed_program, new_program, parsed_program[index])
    
#     walk(parsed_program, new_program, parsed_program[index])
        
#     return new_program

    

def parsProgram(program: Program):
    parsed_program = []

    def walk(node: Node):
        match node.node_type:
            case NodeType.SCOPE:
                for child in node.children_nodes:
                    walk(child)
            case NodeType.TERMINAL:
                parsed_program.append(node.value)
            case NodeType.VAR | NodeType.CONST:
                parsed_program.append((node.name, node.value))
            case NodeType.INPUT:
                parsed_program.append(node.node_type.name)
                for child in node.value:
                    walk(child)
            case NodeType.OUTPUT:
                parsed_program.append(node.node_type.name)
                for child in node.value:
                    walk(child)
            case NodeType.ASSIGNMENT:
                parsed_program.extend([node.node_type.name, node.var_name, "="])
                walk(node.value)
            case NodeType.EXPRESSION:
                parsed_program.append(node.node_type.name)
                walk(node.left)
                walk(node.right)
            case NodeType.FACTOR:
                parsed_program.append(node.node_type.name)
                walk(node.left)
                parsed_program.append(node.operator)
                walk(node.right)

    for child in program.ROOT.children_nodes:
        walk(child)
    
    return parsed_program