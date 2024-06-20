pip install Flask
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate_tax():
    data = request.get_json()
    income = data.get('income', 0)

    # Simple tax calculation logic
    if income <= 10000:
        tax = 0
    elif income <= 20000:
        tax = (income - 10000) * 0.1
    elif income <= 50000:
        tax = 1000 + (income - 20000) * 0.2
    else:
        tax = 7000 + (income - 50000) * 0.3

    return jsonify({'tax': tax})

if __name__ == '__main__':
    app.run(debug=True)
