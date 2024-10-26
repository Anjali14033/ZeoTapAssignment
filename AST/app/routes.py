from flask import Blueprint, request, jsonify
from app.models import Rule, db
from app.utils import Node

main = Blueprint('main', __name__)

@main.route('/create_rule', methods=['POST'])
def api_create_rule():
    rule_string = request.json.get('rule_string')
    rule = Node.create_rule(rule_string)
    db_rule = Rule(rule_string=rule_string)
    db.session.add(db_rule)
    db.session.commit()
    return jsonify({'message': 'Rule created successfully'})

@main.route('/combine_rules', methods=['POST'])
def api_combine_rules():
    rule_ids = request.json.get('rule_ids')
    rules = [Node.create_rule(Rule.query.get(rid).rule_string) for rid in rule_ids]
    combined_rule = Node.combine_rules(rules)
    return jsonify({'combined_rule': str(combined_rule)})

@main.route('/evaluate_rule', methods=['POST'])
def api_evaluate_rule():
    rule_id = request.json.get('rule_id')
    data = request.json.get('data')
    rule_string = Rule.query.get(rule_id).rule_string
    rule = Node.create_rule(rule_string)
    result = Node.evaluate_rule(rule, data)
    return jsonify({'result': result})
