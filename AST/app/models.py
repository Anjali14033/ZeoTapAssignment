from app import db

class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rule_string = db.Column(db.String, nullable=False)  # Original rule as a string
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
