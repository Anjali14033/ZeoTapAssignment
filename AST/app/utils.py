import ast

class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # "operator" or "operand"
        self.left = left  # Left child (for operators)
        self.right = right  # Right child (for operators)
        self.value = value  # The value (for operand nodes)

    def __repr__(self):
        if self.node_type == "operand":
            return f"{self.value}"
        return f"({self.left} {self.value} {self.right})"

    @staticmethod
    def parse_condition(condition):
        # Parses a condition like 'age > 30' or "department = 'Sales'" into a Node
        field, operator, value = condition.strip().split()

        # Check if the value is numeric; if so, convert it to an integer
        if value.isdigit():
            value = int(value)
        else:
            # Remove quotes if it's a string value
            value = value.strip("'\"")

        return Node("operand", value=(field, operator, value))

    @staticmethod
    def create_rule(rule_string):
        # Parse the rule string and build an AST
        # Example: ((age > 30 AND department = 'Sales') OR ...)
        
        # Simplistic parser for demonstration. Use real parsers for complex rules.
        # Split by top-level AND/OR only for the example.
        
        if ' AND ' in rule_string:
            left_part, right_part = rule_string.split(' AND ', 1)
            left_node = Node.create_rule(left_part)
            right_node = Node.create_rule(right_part)
            return Node("operator", left=left_node, right=right_node, value="AND")
        elif ' OR ' in rule_string:
            left_part, right_part = rule_string.split(' OR ', 1)
            left_node = Node.create_rule(left_part)
            right_node = Node.create_rule(right_part)
            return Node("operator", left=left_node, right=right_node, value="OR")
        else:
            return Node.parse_condition(rule_string)

    @staticmethod
    def combine_rules(rules, operator="AND"):
        # Takes a list of AST nodes and combines them
        if not rules:
            return None
        root = rules[0]
        for rule in rules[1:]:
            root = Node("operator", left=root, right=rule, value=operator)
        return root

    @staticmethod
    def evaluate_condition(node, data):
        # Evaluates a condition node against the provided data
        field, operator, value = node.value
        if field not in data:
            return False
        if operator == ">":
            return data[field] > value
        elif operator == "<":
            return data[field] < value
        elif operator == "=":
            return data[field] == value
        return False

    @staticmethod
    def evaluate_rule(ast, data):
        # Recursively evaluates the AST for the given data
        if ast.node_type == "operand":
            return Node.evaluate_condition(ast, data)
        elif ast.node_type == "operator":
            if ast.value == "AND":
                return Node.evaluate_rule(ast.left, data) and Node.evaluate_rule(ast.right, data)
            elif ast.value == "OR":
                return Node.evaluate_rule(ast.left, data) or Node.evaluate_rule(ast.right, data)
        return False

