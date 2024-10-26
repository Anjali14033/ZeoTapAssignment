from app import create_app, db

# Create the Flask app
app = create_app()

# Ensure database tables are created
with app.app_context():
    db.create_all()

# Start the app
if __name__ == '__main__':
    app.run(debug=True, port=8000)
