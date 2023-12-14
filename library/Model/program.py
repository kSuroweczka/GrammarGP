import os
import random
from library.Tasks.task import Task, TestCase
from library.Model.node import *
from library.Solver.params import Params

class Program():
    id: int
    name: str
    variables: dict[str, VarNode]
    input_data: list[float]
    output_data: list[float]
    const: list[float]
    task: Task
    fitness: float
    mutable_nodes = list[Node]
    max_depth: int
    min_rand: int
    max_rand: int
    ROOT: ScopeNode


    def __init__(self, id: int, task: Task, max_depth: int, min_rand: int = -5, max_rand: int = 5, input_data: list[float] = []):
        self.id = id
        self.task = task
        self.name = task.name
        self.variables = {}
        self.const = []
        self.input_data = input_data
        self.output_data = []
        self.mutable_nodes = []
        self.fitness = 0.0
        self.max_depth = max_depth
        self.min_rand = min_rand
        self.max_rand = max_rand
        self.ROOT = ScopeNode(NodeType.SCOPE, None, [])
        self.input_index = 0


    def __repr__(self):
        print(self.ROOT)
        return ""

    # TO DO
    def runProgram(self, node: Node):
        match node.node_type:
            case NodeType.Input:
                pass


    #TO DO
    def growTree(self):
        posible_nodes = [NodeType.ASSIGNMENT, NodeType.OUTPUT, NodeType.IF, NodeType.WHILE]
        node_t = random.choice(posible_nodes)

        for i in range(random.randint(3, 5)):
            self.ROOT.add_child(self.createNode(node_t, self.ROOT))

        

    def createIndividual(self):  

        self.growTree()
        # self.runProgram(self.ROOT)



    def createNode(self, type: NodeType, parent: Node, current_depth: int = 0):
        if type == NodeType.INPUT:
            input = InputNode(node_type=type, parent_node=parent)
            if self.input_index == self.input_data.__len__():
                self.input_index = 0
            value = self.input_data[self.input_index]
        
            input.value = value
            self.input_index += 1
            return input
        
        elif type == NodeType.OUTPUT:
            const_count = self.const.__len__()
            var_count = self.variables.__len__()

            output = OutputNode(node_type=type, parent_node=parent, children_nodes=[])
            output.depth = current_depth

            choice = random.choice(["var", "const", "rand"])
            out_rand = choice == "rand"
            out_const = choice == "const"
            out_var = choice == "var"

            if (var_count == 0 and const_count == 0) or out_rand or (const_count == 0 and out_const) or (var_count == 0 and out_var):
                rand_value = float(random.randint(self.min_rand, self.max_rand))
                output.add_child(rand_value)
                self.output_data.append(rand_value)
                self.const.append(rand_value)
            elif out_const:
                rand_const = random.choice(list(self.const))
                output.add_child(rand_const)
                self.output_data.append(rand_const)
            else:
                rand_var = random.choice(list(self.variables.keys()))
                var = self.variables[rand_var]
                output.add_child(var)
                self.output_data.append(var.value)

            output.value = output.calculate()
            return output
        

        elif type == NodeType.VAR:
            var_name = f"x_{self.variables.__len__()}"
            choice = random.choice(['number', 'bool'])
            if choice == 'number':
                rand_value = float(random.randint(self.min_rand, self.max_rand))
                node = VarNode(node_type=type, parent_node=parent, name=var_name, value=rand_value)
            else:
                rand_value = random.choice([True, False])            
                node = VarNode(node_type=type, parent_node=parent, name=var_name, value=rand_value)
            
            return node
            
            
        elif type == NodeType.ASSIGNMENT:
            create_var = self.variables.__len__() == 0
            action = random.choice(["create", "assign"])
            body_type = random.choice(["exp", "input"])

            print(f'{action} {body_type}')
            match action, create_var:
                case ("create", True|False) | ("assign", True):
                    new_var = self.createNode(NodeType.VAR, None, current_depth+1)
                    match body_type:
                        case "exp":
                            exp = self.createNode(NodeType.EXPRESSION, None, current_depth+1)
                            new_var.value = exp.value
                            assign = AssignmentNode(node_type=type, parent_node=parent, var=new_var, body=exp)
                            assign.depth = current_depth
                            new_var.parent_node = assign
                            exp.parent_node = assign
                            assign.add_child(new_var)
                            assign.add_child(exp)
                        case "input":
                            input = self.createNode(NodeType.INPUT, None, current_depth+1)
                            new_var.value = input.value
                            assign = AssignmentNode(node_type=type, parent_node=parent, var=new_var, body=input)
                            assign.add_child(new_var)
                            assign.add_child(input)
                    self.variables.update({new_var.name: new_var})
                
                case "assign", False:
                    new_var = self.createNode(NodeType.VAR, None, current_depth+1)
                    match body_type:
                        case "exp":
                            exp = self.createNode(NodeType.EXPRESSION, None, current_depth+1)
                            new_var.value = exp.value
                            assign = AssignmentNode(node_type=type, parent_node=parent, var=new_var, body=exp)
                            assign.depth = current_depth
                            exp.parent_node = assign
                            assign.add_child(new_var)
                            assign.add_child(exp)
                        case "input":
                            input = self.createNode(NodeType.INPUT, None, current_depth+1)
                            new_var.value = input.value
                            assign = AssignmentNode(node_type=type, parent_node=parent, var=new_var, body=input)
                            assign.add_child(new_var)
                            assign.add_child(input)
            
            return assign


            
            # elif create_bool:
            #     new_var = self.createNode(NodeType.VAR, None, current_depth+1)
            #     choice2 = random.choice(['bool', 'cond'])
            #     if choice2 == 'bool':
            #         bool = self.createNode(NodeType.BOOLEAN, parent=parent)
            #         new_var.value = bool.value
            #         assign = AssignmentNode(node_type=type, parent_node=parent, var=new_var, body=bool.value)
            #         assign.add_child(new_var)
            #         assign.add_child(bool)
            #         return assign
            #     if choice2 == 'cond':
            #         condNode = self.createNode(NodeType.CONDITION, parent=parent)
            #         new_var.add_child(condNode)
            #         assign = AssignmentNode(node_type=type, parent_node=parent, var=new_var, body=condNode)
            #         assign.add_child(new_var)
            #         assign.add_child(condNode)
                    
        elif type == NodeType.EXPRESSION:
            left = self.createNode(NodeType.TERM, None, current_depth+1)
            right = random.choice([
                self.createNode(NodeType.TERM, None, current_depth+1),
                None])
            
            if right is None:
                operation = None
            else:
                operation = random.choice(['+', '-'])

            out = ExpressionNode(node_type=type, parent_node=parent, left=left, right=right, operation=operation, children_nodes=[])
            out.depth = current_depth
            left.parent_node = out
            if right != None:
                right.parent_node= out
            out.add_child(left)
            out.add_child(right)
            
            self.mutable_nodes.append(out)
            return out
        
        elif type == NodeType.TERM:
            left = self.createNode(NodeType.FACTOR, None, current_depth+1)
            right = random.choice([
                self.createNode(NodeType.FACTOR, None, current_depth+1),
                None])
            
            if right is None:
                operation = None
            else:
                operation = random.choice(['*', '/'])
            
            out = TermNode(node_type=type, parent_node=parent, left=left, right=right, operation=operation, children_nodes=[])
            out.depth = current_depth
            left.parent_node = out
            if right != None:
                right.parent_node = out
            out.add_child(left)
            out.add_child(right)

            self.mutable_nodes.append(out)
            return out
        
        elif type == NodeType.FACTOR:
            count_var = self.variables.__len__()
            count_const = self.const.__len__()

            choice = random.choice(["var", "const", "rand", "exp"])
            out_exp = choice == "exp"
            out_rand = choice == "rand"
            out_const = choice == "const"
            out_var = choice == "var"

            if out_exp and current_depth < self.max_depth-2:
                out = self.createNode(NodeType.EXPRESSION, parent, current_depth+1)
            elif (count_var == 0 and count_const == 0) or out_rand or (count_const == 0 and out_const) or (count_var == 0 and out_var):
                value = float(random.randint(self.min_rand, self.max_rand)) 
                out = FactorNode(node_type=type, parent_node=parent, body=value, children_nodes=[])
                out.depth = current_depth
                out.add_child(value)
            elif out_const:
                rand_const = random.choice(list(self.const.keys()))
                const = self.const[rand_const]
                out = FactorNode(node_type=type, parent_node=parent, body=const, children_nodes=[])
                out.depth = current_depth
                out.add_child(const)
            else:
                rand_var = random.choice(list(self.variables.keys()))
                var = self.variables[rand_var]
                out = FactorNode(node_type=type, parent_node=parent, body=var, children_nodes=[])
                out.depth = current_depth
                out.add_child(var)


            self.mutable_nodes.append(out)
            return out
        
        elif type == NodeType.BOOLEAN:
            boolean = random.choice([True, False])
            booleanNode = BooleanNode(node_type=type, parent_node=parent,value=boolean)
            booleanNode.depth = current_depth
            return booleanNode
        

        elif type == NodeType.EXPRESSIONCONDITION:
            children = []
            leftexpNode = self.createNode(NodeType.EXPRESSION, parent=None, current_depth=current_depth+1)
            children.append(leftexpNode)
            operator = random.choice(['==', '!=','<','>','<=' ,'>='])

            rightexpNode = self.createNode(NodeType.EXPRESSION, parent=None, current_depth=current_depth+1)
            children.append(rightexpNode)

            expressionConditionNode = ExpressionConditionNode(node_type=type, 
                                                              parent_node=parent,
                                                              children_nodes=children,
                                                              leftExpression=leftexpNode,
                                                              rigthExpression=rightexpNode,
                                                              operator = operator)
            expressionConditionNode.depth = current_depth
            leftexpNode.parent_node = expressionConditionNode
            rightexpNode.parent_node = expressionConditionNode
            return expressionConditionNode

        elif type == NodeType.LOGICCONDITION:
            children = []
            leftBoolean = self.createNode(NodeType.BOOLEAN, parent= None,current_depth=current_depth+1)
            children.append(leftBoolean)

            operator = random.choice(['!=', '=='])

            rightBoolean = self.createNode(NodeType.BOOLEAN, parent= None,current_depth=current_depth+1)
            children.append(rightBoolean)

            LogicConditionNode = LogicCondition(node_type=type, 
                                                parent_node=parent,
                                                children_nodes=children,
                                                leftBoolean=leftBoolean,
                                                rightBoolean=rightBoolean,
                                                operator=operator
                                                )
            LogicConditionNode.depth = current_depth
            leftBoolean.parent_node = LogicConditionNode
            rightBoolean.parent_node = LogicConditionNode

            return LogicConditionNode
        
        elif type == NodeType.CONDITION:
            howMuch = random.choice([1,2])  ### potem dodac 3 i 4
            children =[]
            logicOperators = []
            expOrlog = random.choice(['exp', 'log'])
            if expOrlog == 'exp':
                expressionConditionNode = self.createNode(NodeType.EXPRESSIONCONDITION,  None, current_depth+1)
                children.append(expressionConditionNode)
            if expOrlog == 'log':
                logicConditionNode = self.createNode(NodeType.LOGICCONDITION, None, current_depth+1)
                children.append(logicConditionNode)

            for i in range(howMuch-1):
                expOrlog = random.choice(['exp', 'log'])
                logicOperator = random.choice(["&&", "||"])
                logicOperators.append(logicOperator)
                # logicOperator = self.createNode(NodeType.LOGICOPERATOR, parent, current_depth)
                # children.append(logicOperator)
                if expOrlog == 'exp':
                    expressionConditionNode = self.createNode(NodeType.EXPRESSIONCONDITION,  None, current_depth+1)
                    children.append(expressionConditionNode)
                if expOrlog == 'log':
                    logicConditionNode = self.createNode(NodeType.LOGICCONDITION, None, current_depth+1)
                    children.append(logicConditionNode)

            conditionNode = ConditionNode(node_type=type, 
                                          parent_node= parent, 
                                          children_nodes=children,
                                          logicOperators = logicOperators)
            conditionNode.depth = current_depth
            for child in children:
                child.parent_node = conditionNode

            return conditionNode

        
        elif type == NodeType.SCOPE:
            howMuch = random.choice([1,2])
            scope = ScopeNode(node_type=type, parent_node=parent, children_nodes=[])

            for i in range(howMuch):
                # choice = random.choice(['if', 'assignment']) # potem dodac loopstatement
                choice = random.choice(['assignment', 'if']) ## na razie tak bo sie robie nieskonczona petla
                if choice == 'if' and current_depth < self.max_depth-2:
                    ifNode = self.createNode(NodeType.IF, scope, current_depth+1)
                    scope.add_child(ifNode)
                if choice == 'assignment' or current_depth >= self.max_depth-2:
                    assignmentNode = self.createNode(NodeType.ASSIGNMENT, scope, current_depth+1)
                    scope.add_child(assignmentNode)

            scope.depth = current_depth
            return scope

        
        elif type == NodeType.IF:
            children = []
            ifNode = IfNode(node_type=type,
                            parent_node= parent, 
                            children_nodes=children)
            
            condition = self.createNode(NodeType.CONDITION, None, current_depth+1)
            ifNode.add_child(condition)
            ifNode.conditionNode = condition

            ifTrueBody = self.createNode(NodeType.SCOPE, None, current_depth+1)
            ifNode.add_child(ifTrueBody)
            ifNode.ifBodyNode = ifTrueBody

            choice = random.choice([True, False])
            if choice == True:
                ifFalseBody = self.createNode(NodeType.SCOPE, None, current_depth+1)
                ifNode.add_child(ifFalseBody)
                ifNode.elseBodyNode = ifFalseBody

                ifNode.depth = current_depth


            ifNode.depth = current_depth


            return ifNode
        
        elif type == NodeType.WHILE:
            children =[]
            conditionNode = self.createNode(NodeType.CONDITION, None, current_depth+1)
            children.append(conditionNode)
            compoundStatementNode = self.createNode(NodeType.SCOPE, None, current_depth+1)
            children.append(compoundStatementNode)

            whileNode = WhileNode(node_type=type, 
                                  parent_node= parent, 
                                  children_nodes=children, 
                                  conditionNode=conditionNode, 
                                  whileBodyNode=compoundStatementNode)
            whileNode.depth = current_depth
            for child in children:
                child.parent_node= whileNode


            return whileNode
        

    def serialize(self, node: Node):
        for child in node.children_nodes:
            if type(child) != float and child.node_type != None:
                branch=""
                for i in range(node.depth):
                    branch += "-"
                print(branch, child, child.node_type)
                self.serialize(child)
            else:
                branch=""
                for i in range(self.max_depth):
                    branch += "-"

                print(branch, child)