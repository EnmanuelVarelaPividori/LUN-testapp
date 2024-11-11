from flask import Flask
from app import create_app
from app.utils.db_connection import db

app = Flask(__name__)
app = create_app()

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)