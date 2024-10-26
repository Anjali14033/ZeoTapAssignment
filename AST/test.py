from app.utils import Node
# Test Case Example
rule1 = Node.create_rule("age > 30 AND department = 'Sales'")
rule2 = Node.create_rule("salary > 50000 OR experience > 5")
combined_rule = Node.combine_rules([rule1, rule2])

# Test evaluation
data = {"age": 35, "department": "Sales", "salary": 20000, "experience": 6}
print(Node.evaluate_rule(combined_rule, data))  # Should return True based on rule
