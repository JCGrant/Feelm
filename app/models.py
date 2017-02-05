from app import db

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    numViewingSessions = db.Column(db.Integer)
    avgAnger = db.Column(db.Float)
    avgContempt = db.Column(db.Float)
    avgDisgust = db.Column(db.Float)
    avgFear = db.Column(db.Float)
    avgHappiness = db.Column(db.Float)
    avgNeutral = db.Column(db.Float)
    avgSadness = db.Column(db.Float)
    avgSuprise = db.Column(db.Float)

class EmotionTimeFrame(db.Model):
    seconds = db.Column(db.Integer, primary_key=True)
    film = db.relationship('Film', backref='time_frames', lazy='dynamic')
    anger = db.Column(db.Float)
    contempt = db.Column(db.Float)
    disgust = db.Column(db.Float)
    fear = db.Column(db.Float)
    happiness = db.Column(db.Float)
    neutral = db.Column(db.Float)
    sadness = db.Column(db.Float)
    suprise = db.Column(db.Float)
