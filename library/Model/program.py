import os
import random
from library.Tasks.task import Task, TestCase
from library.Model.node import *
from library.Solver.params import Params

class Program():
    id: int
    name: str
    task: Task
    variables: dict[str, VarNode]
    const: dict[str, ConstNode]
    input_data: list[float]
    output_data: list[float]
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
        self.const = {}
        self.input_data = input_data
        self.output_data = []
        self.mutable_nodes = []
        self.fitness = 0.0
        self.max_depth = max_depth
        self.min_rand = min_rand
        self.max_rand = max_rand
        self.ROOT = ScopeNode(NodeType.SCOPE, None, [])


    def __repr__(self):
        for child in self.ROOT.children_nodes:
            print(child)
        return ""

    def createIndividual(self):        
        self.ROOT.add_child(self.createNode(NodeType.INPUT, self.ROOT))

        self.ROOT.add_child(self.createNode(NodeType.ASSIGNMENT, self.ROOT))

        # posible_nodes = [NodeType.ASSIGNMENT, NodeType.VAR, NodeType.CONST]
        # node_t = random.choice(posible_nodes)

        # for i in range(random.randint(2, 5)):
        #     self.ROOT.add_child(self.createNode(node_t, self.ROOT))

        # self.ROOT.add_child(self.createNode(NodeType.CONDITION, self.ROOT))

        self.ROOT.add_child(self.createNode(NodeType.IF, self.ROOT))

        self.ROOT.add_child(self.createNode(NodeType.OUTPUT, self.ROOT))
        


    def createNode(self, type: NodeType, parent: Node, current_depth: int = 0):


        if type == NodeType.INPUT:
            input_len = len(self.input_data)
            input = InputNode(node_type=type, parent_node=parent, children_nodes=[])

            for i in range(input_len):
                new_assignment = self.createNode(NodeType.ASSIGNMENT, input, current_depth)
                input.add_child(new_assignment)

            input.value = input.calculate()
            return input
        
        
        elif type == NodeType.OUTPUT:
            const_count = self.const.__len__()
            var_count = self.variables.__len__()

            output = OutputNode(node_type=type, parent_node=parent, children_nodes=[])
            output_len = random.randint(self.task.min_output_length, self.task.max_output_length)

            for i in range(output_len):
                choice = random.choice(["var", "const", "rand"])
                out_rand = choice == "rand"
                out_const = choice == "const"
                out_var = choice == "var"

                if (var_count == 0 and const_count == 0) or out_rand or (const_count == 0 and out_const) or (var_count == 0 and out_var):
                    rand_value = float(random.randint(self.min_rand, self.max_rand))
                    output.add_child(rand_value)
                    self.output_data.append(rand_value)
                elif out_const:
                    rand_const = random.choice(list(self.const.keys()))
                    const = self.const[rand_const]
                    output.add_child(const)
                    self.output_data.append(const.value)
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
                node = VarNode(node_type=type, parent_node=None, name=var_name, value=rand_value)
            else:
                boolNode = self.createNode(NodeType.BOOLEAN, parent= parent)
                node = VarNode(node_type=type, parent_node=None, name=var_name, value=boolNode.value)
                # node.add_child(boolNode)
            
            return node
            
        elif type == NodeType.CONST:
            const_name = f"c_{self.const.__len__()}"
            rand_value = float(random.randint(self.min_rand, self.max_rand))
            node = ConstNode(node_type=type, parent_node=None, name=const_name, value=rand_value)
            
            return node
            
        elif type == NodeType.ASSIGNMENT:
            var_count = self.variables.__len__()
            
            # only for input node
            if parent.node_type == NodeType.INPUT:
                index = self.variables.__len__()
                var_value = float(self.input_data[index])

                new_var = self.createNode(NodeType.VAR, None, current_depth+1)
                new_var.value = var_value

                assign = AssignmentNode(node_type=type, parent_node=parent, var=new_var, body=var_value, children_nodes=[])
                assign.add_child(new_var)
                assign.add_child(var_value)
                self.variables.update({new_var.name: new_var})

            else:
                choice = random.choice(["var", "const", "assign"])
                create_const = choice == "const"
                create_var = choice == "var"
                var_assign = choice == "assign"
                # create_bool = choice == "bool"

                if create_const:
                    new_const = self.createNode(NodeType.CONST, None, current_depth+1)
                    exp = self.createNode(NodeType.EXPRESSION, None, current_depth+1)
                    new_const.value = exp.value

                    assign = AssignmentNode(node_type=type, parent_node=parent, var=new_const, body=exp)
                    assign.add_child(new_const)
                    assign.add_child(exp)

                    self.const.update({new_const.name: new_const})

                elif create_var:
                    new_var = self.createNode(NodeType.VAR, None, current_depth+1)
                    exp = self.createNode(NodeType.EXPRESSION, None, current_depth+1)
                    new_var.value = exp.value

                    assign = AssignmentNode(node_type=type, parent_node=parent, var=new_var, body=exp)
                    assign.add_child(new_var)
                    assign.add_child(exp)

                    self.variables.update({new_var.name: new_var})

                elif var_assign:
                    var_name = random.choice(list(self.variables.keys()))
                    var = self.variables[var_name]
                    exp = self.createNode(NodeType.EXPRESSION, None, current_depth+1)
                    var.value = exp.value

                    assign = AssignmentNode(node_type=type, parent_node=parent, var=var, body=exp)
                    assign.add_child(var)
                    assign.add_child(exp)
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
            return assign
                    
        elif type == NodeType.EXPRESSION:
            left = self.createNode(NodeType.TERM, parent, current_depth+1)
            right = random.choice([
                self.createNode(NodeType.TERM, parent, current_depth+1),
                None])
            
            if right is None:
                operation = None
            else:
                operation = random.choice(['+', '-'])

            out = ExpressionNode(node_type=type, parent_node=parent, left=left, right=right, operation=operation, children_nodes=[])
            out.add_child(left)
            out.add_child(right)
            
            self.mutable_nodes.append(out)
            return out
        
        elif type == NodeType.TERM:
            left = self.createNode(NodeType.FACTOR, parent, current_depth+1)
            right = random.choice([
                self.createNode(NodeType.FACTOR, parent, current_depth+1),
                None])
            
            if right is None:
                operation = None
            else:
                operation = random.choice(['*', '/'])
            
            out = TermNode(node_type=type, parent_node=parent, left=left, right=right, operation=operation, children_nodes=[])
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
                out.add_child(value)
            elif out_const:
                rand_const = random.choice(list(self.const.keys()))
                const = self.const[rand_const]
                out = FactorNode(node_type=type, parent_node=parent, body=const, children_nodes=[])
                out.add_child(const)
            else:
                rand_var = random.choice(list(self.variables.keys()))
                var = self.variables[rand_var]
                out = FactorNode(node_type=type, parent_node=parent, body=var, children_nodes=[])
                out.add_child(var)


            self.mutable_nodes.append(out)
            return out
        
        elif type == NodeType.BOOLEAN:
            boolean = random.choice([True, False])
            booleanNode = BooleanNode(node_type=type, parent_node=parent,value=boolean)
            return booleanNode
        
        elif type == NodeType.OPERATOR:
            operator = random.choice(['==', '!=','<','>','<=' ,'>='])
            operatorNode=OperatorNode(node_type=type, parent_node=parent, operatorType=operator)
            return operatorNode
        
        elif type==NodeType.LOGICOPERATOR:
            operator= random.choice(["&&", "||"])
            logicOperatorNode = LogicOperator(node_type=type, parent_node=parent, operatorType=operator)
            return logicOperatorNode
        
        elif type == NodeType.EXPRESSIONCONDITION:
            children = []
            leftexpNode = self.createNode(NodeType.EXPRESSION, parent=parent)
            children.append(leftexpNode)
            operatorNode = self.createNode(NodeType.OPERATOR, parent = parent)
            children.append(operatorNode)
            rightexpNode = self.createNode(NodeType.EXPRESSION, parent=parent)
            children.append(rightexpNode)

            expressionConditionNode = ExpressionConditionNode(node_type=type, parent_node=parent,children_nodes=children)
            return expressionConditionNode

        elif type == NodeType.LOGICCONDITION:
            children = []
            leftBoolean = self.createNode(NodeType.BOOLEAN, parent= parent)
            children.append(leftBoolean)

            operator = random.choice(['!=', '=='])
            operator = OperatorNode(node_type=NodeType.OPERATOR, parent_node=parent, operatorType=operator)
            children.append(operator)

            rightBoolean = self.createNode(NodeType.BOOLEAN, parent= parent)
            children.append(rightBoolean)

            LogicConditionNode = LogicCondition(node_type=type, parent_node=parent,children_nodes=children)

            return LogicConditionNode
        
        elif type == NodeType.CONDITION:
            howMuch = random.choice([1,2,3,4])
            children =[]

            expOrlog = random.choice(['exp', 'log'])
            if expOrlog == 'exp':
                expressionConditionNode = self.createNode(NodeType.EXPRESSIONCONDITION,  parent, current_depth)
                children.append(expressionConditionNode)
            if expOrlog == 'log':
                logicConditionNode = self.createNode(NodeType.LOGICCONDITION, parent, current_depth)
                children.append(logicConditionNode)

            for i in range(howMuch-1):
                expOrlog = random.choice(['exp', 'log'])
                logicOperator = self.createNode(NodeType.LOGICOPERATOR, parent, current_depth)
                children.append(logicOperator)
                if expOrlog == 'exp':
                    expressionConditionNode = self.createNode(NodeType.EXPRESSIONCONDITION,  parent, current_depth)
                    children.append(expressionConditionNode)
                if expOrlog == 'log':
                    logicConditionNode = self.createNode(NodeType.LOGICCONDITION, parent, current_depth)
                    children.append(logicConditionNode)

            conditionNode = ConditionNode(node_type=type, parent_node= parent, children_nodes=children)

            return conditionNode

        elif type == NodeType.COMPOUNDSTATEMENT:
            howMuch = random.choice([1,2])
            children=[]
            for i in range(howMuch):
                # choice = random.choice(['if', 'assignment', 'compoundStatement']) # potem dodac loopstatement
                choice = random.choice(['assignment']) ## na razie tak bo sie robie nieskonczona petla
                if choice == 'if':
                    ifNode = self.createNode(NodeType.IF, parent, current_depth)
                    children.append(ifNode)
                if choice == 'assignment':
                    assignmentNode = self.createNode(NodeType.ASSIGNMENT, parent, current_depth)
                    children.append(assignmentNode)
                # if choice == 'compoundStatement':
                #     compoundNode = self.createNode(NodeType.COMPOUNDSTATEMENT,  parent, current_depth)
                #     children.append(compoundNode)
            compoundNode = CompoundStatementNode(node_type=type, parent_node= parent, children_nodes=children)
            return compoundNode
        
        elif type == NodeType.IF:
            children = []

            conditionNode = self.createNode(NodeType.CONDITION, parent, current_depth)
            children.append(conditionNode)

            compoundStatementNode = self.createNode(NodeType.COMPOUNDSTATEMENT, parent, current_depth)
            children.append(compoundStatementNode)

            choice = random.choice([True, False])
            if choice == True:
                compoundStatementNode2 = self.createNode(NodeType.COMPOUNDSTATEMENT, parent, current_depth)
                children.append(compoundStatementNode2)
                ifNode = IfNode(node_type=type,
                                parent_node= parent, 
                                children_nodes=children,
                                conditionNode=conditionNode, 
                                ifBody=compoundStatementNode,
                                elseBody=compoundStatementNode2)
            else:
                ifNode = IfNode(node_type=type,
                                parent_node= parent, 
                                children_nodes=children,
                                conditionNode=conditionNode, 
                                ifBody=compoundStatementNode)
            return ifNode
        
        elif type == NodeType.WHILE:
            children =[]
            conditionNode = self.createNode(NodeType.CONDITION, parent, current_depth)
            children.append(conditionNode)
            compoundStatementNode = self.createNode(NodeType.COMPOUNDSTATEMENT, parent, current_depth)
            children.append(compoundStatementNode)

            whileNode = WhileNode(node_type=type, 
                                  parent_node= parent, 
                                  children_nodes=children, 
                                  conditionNode=conditionNode, 
                                  whileBodyNode=compoundStatementNode)

            return whileNode