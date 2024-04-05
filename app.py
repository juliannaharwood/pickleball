from flask import Flask, render_template, request, jsonify, json
from backend import train
import pandas as pd

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show_data', methods=['POST'])
def show_data():
    pickle_raw = train.load_data()
    pickle_clean = train.clean_data(pickle_raw)
    pickle_clean = train.feature_engineer(pickle_clean)
    data = request.get_json()
    selected_value = data['value']
    # Process the selected value as needed
    final_data = train.get_data(pickle_clean, int(selected_value))
    print(final_data['Game Length'])
    return jsonify(str(final_data['Game Length']))

if __name__ == '__main__':
    app.run(debug=True)