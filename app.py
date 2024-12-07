from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)


# Route to serve the dashboard page
@app.route('/')
def dashboard():
    try:
        # Read the JSON file
        with open('detection.json', 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = {"message": "No detections available yet."}

    # Render the template with data
    return render_template('dashboard.html', inventory=data)


# API route to get JSON data
@app.route('/api/inventory')
def get_inventory():
    try:
        with open('detections.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"error": "No detections.json file found"}

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
