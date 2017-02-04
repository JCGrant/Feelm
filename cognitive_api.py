import requests

EMOTION_API_URL = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize'
FACE_API_URL_BASE = 'https://westus.api.cognitive.microsoft.com/face/v1.0/'
DETECT_FACE_API_URL = FACE_API_URL_BASE + 'detect'
IDENTIFY_FACE_API_URL = FACE_API_URL_BASE + 'identify'


class CognitiveApi:

    def __init__(self, keys):
        self.keys = {}
        for service, key in keys.items():
            self.keys[service] = key

    def detect_emotions(self, url):
        json = { 'url': url }
        headers = { 'Ocp-Apim-Subscription-Key': self.keys['emotion'] }
        response = requests.post(EMOTION_API_URL, json=json, headers=headers)
        return response.json()
