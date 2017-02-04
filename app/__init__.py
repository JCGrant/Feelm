import os
from flask import Flask

app = Flask(__name__)
app.config['COGNITIVE_URL'] = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize'
app.config['COGNITIVE_KEY'] = os.environ['COGNITIVE_KEY']

from app import views
