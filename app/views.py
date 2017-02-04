from flask import render_template, jsonify
from app import app, cognitive_api
import requests

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/process/<path:url>', methods=['POST'])
def process(url):
    emotion_json = cognitive_api.detect_emotions(url)
    return jsonify(emotion_json)
