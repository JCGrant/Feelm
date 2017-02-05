import os
from flask import Flask
from cognitive_api import CognitiveApi

app = Flask(__name__)

cognitive_api = CognitiveApi({
    'emotion': os.environ['COGNITIVE_EMOTION_API_KEY'],
    'face': os.environ['COGNITIVE_FACE_API_KEY'],
})


from app import views
