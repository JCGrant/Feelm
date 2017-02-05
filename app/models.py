from app import db

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),unique=True)
    NoOfViewingSessions = db.Column(db.Integer)
    emotionalTimeframes = db.relationship('Emotion', backref='film', lazy='dynamic')
    averageAnger = db.Column(db.Float)
    averageHappiness = db.Column(db.Float)
    averageSuprise = db.Column(db.Float)
    averageDisgust = db.Column(db.Float)

class Emotion(db.Model):
    Seconds = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    Anger = db.Column(db.Float)
    Happiness = db.Column(db.Float)
    Suprise = db.Column(db.Float)
    Disgust = db.Column(db.Float)