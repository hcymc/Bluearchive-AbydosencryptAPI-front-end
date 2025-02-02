from flask import Flask, request, render_template, jsonify
import math
from datetime import datetime
import requests
from flask import Flask, render_template, request
import requests

app = Flask(__name__)
def get_api_key():
    current_seconds = int((datetime.now() - datetime(1970, 1, 1)).total_seconds())
    return math.floor(current_seconds + math.sqrt(current_seconds))

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/callapi', methods=['POST'])
def callapi():
    API = request.form.get('api')
    TEXT = request.form.get('text')
    key = get_api_key()
    url = f'http://localhost:5000/{API}?input={TEXT}&key={key}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return jsonify(result=response.json().get("result"))
        else:
            return jsonify(error=response.status_code, message=response.text), response.status_code
    except Exception as e:
        return jsonify(error='Internal Server Error', message=str(e)), 500


if __name__ == '__main__':
    app.run(port=577)   