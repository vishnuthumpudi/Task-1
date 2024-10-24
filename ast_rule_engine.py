import re

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
