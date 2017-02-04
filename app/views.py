from flask import render_template, jsonify
from app import app
import requests

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/process/<path:url>', methods=['POST'])
def process(url):
    api_url = app.config['COGNITIVE_URL']
    api_key = app.config['COGNITIVE_KEY']
    json = { 'url': url }
    headers = { 'Ocp-Apim-Subscription-Key': api_key }
    response = requests.post(api_url, json=json, headers=headers)
    return jsonify(response.json())
