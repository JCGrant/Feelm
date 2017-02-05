import os
from flask import Flask
from cognitive_api import CognitiveApi
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

cognitive_api = CognitiveApi({
    'emotion': os.environ['COGNITIVE_EMOTION_API_KEY'],
    'face': os.environ['COGNITIVE_FACE_API_KEY'],
})


from app import views, models
