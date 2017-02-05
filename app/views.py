from flask import render_template, jsonify, abort
from app import app, cognitive_api
import requests

EMOTIONS = [
    'anger',
    'contempt',
    'disgust',
    'fear',
    'happiness',
    'neutral',
    'sadness',
    'surprise',
]

@app.route('/')
def home():
    return render_template('home.html', emotions=EMOTIONS)

@app.route('/emotion/<emotion>')
def emotions(emotion):
    if emotion not in EMOTIONS:
        abort(404)
    return render_template('emotion.html', emotion=emotion)

@app.route('/process/<path:url>', methods=['POST'])
def process(url):
    emotion_json = cognitive_api.detect_emotions(url)
    return jsonify(emotion_json)
