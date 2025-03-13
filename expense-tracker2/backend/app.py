from flask import Flask
from flask_cors import CORS
from routes import signup, login, add_expense, get_expenses

app = Flask(__name__)
CORS(app)

# Register routes
app.route('/signup', methods=['POST'])(signup)
app.route('/login', methods=['POST'])(login)
app.route('/add_expense', methods=['POST'])(add_expense)
app.route('/get_expenses', methods=['GET'])(get_expenses)

if __name__ == '__main__':
    app.run(debug=True)