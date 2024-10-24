import re

class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.node_type = node_type  # 'operator' or 'operand'
        self.value = value  # operand's value
        self.left = left  
        self.right = right 

    def evaluate(self, data):
        if self.node_type == "operand":
            return self._evaluate_operand(data)
        elif self.node_type == "operator":
            return self._evaluate_operator(data)

    def _evaluate_operand(self, data):
        # Extract key and value from the operand (e.g., "age > 30")
        key, operator, value = self.value.split(" ")
        key_value = data.get(key)

        # Apply comparison based on the operator
        if operator == ">":
            return key_value > int(value)
        elif operator == "<":
            return key_value < int(value)
        elif operator == "=":
            return key_value == value
        return False

    def _evaluate_operator(self, data):
        if self.value == "AND":
            return self.left.evaluate(data) and self.right.evaluate(data)
        elif self.value == "OR":
            return self.left.evaluate(data) or self.right.evaluate(data)
        return False


def parse_rule_string(rule_string):
    # Parse string into AST, tokenizing the rule and constructing nodes.
    tokens = re.split(r'(\W+)', rule_string)
    stack = []
    operators = {"AND", "OR"}

    while tokens:
        token = tokens.pop(0).strip()
        if token.isnumeric() or re.match(r"[\w]+", token):
            stack.append(Node("operand", token))
        elif token in operators:
            right = stack.pop()
            left = stack.pop()
            stack.append(Node("operator", token, left, right))

    return stack[0]  # Return root node of the AST

def create_rule(rule_string):
    # Creates AST from the rule string
    return parse_rule_string(rule_string)

def combine_rules(rules):
    # Combines multiple ASTs into one
    combined_ast = rules[0]
    for rule in rules[1:]:
        combined_ast = Node("operator", "AND", combined_ast, rule)
    return combined_ast

def evaluate_rule(rule_ast, data):
    return rule_ast.evaluate(data)
