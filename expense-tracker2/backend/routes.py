from flask import request, jsonify
from bson.objectid import ObjectId
from models import users_collection, expenses_collection

# Signup Route
def signup():
    data = request.json
    if not data or not all(key in data for key in ['name', 'email', 'password', 'phone']):
        return jsonify({'message': 'Missing fields'}), 400

    # Check if user already exists
    if users_collection.find_one({'email': data['email']}):
        return jsonify({'message': 'User already exists'}), 400

    # Insert new user
    user = {
        'name': data['name'],
        'email': data['email'],
        'password': data['password'],
        'phone': data['phone']
    }
    users_collection.insert_one(user)
    return jsonify({'message': 'User created successfully'}), 201

# Login Route
def login():
    data = request.json
    if not data or not all(key in data for key in ['email', 'password']):
        return jsonify({'message': 'Missing fields'}), 400

    user = users_collection.find_one({'email': data['email'], 'password': data['password']})
    if user:
        return jsonify({'message': 'Login successful', 'user_id': str(user['_id'])}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

# Add Expense Route
def add_expense():
    data = request.json
    if not data or not all(key in data for key in ['user_id', 'amount', 'date', 'category', 'description']):
        return jsonify({'message': 'Missing fields'}), 400

    expense = {
        'user_id': data['user_id'],
        'amount': data['amount'],
        'date': data['date'],
        'category': data['category'],
        'description': data['description']
    }
    expenses_collection.insert_one(expense)
    return jsonify({'message': 'Expense added successfully'}), 201

# Get Expenses Route
def get_expenses():
    user_id = request.args.get('user_id')
    category = request.args.get('category')
    query = {'user_id': user_id}
    if category:
        query['category'] = category
    expenses = list(expenses_collection.find(query))
    for expense in expenses:
        expense['_id'] = str(expense['_id'])
    return jsonify(expenses), 200