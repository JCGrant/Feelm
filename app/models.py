from app import db

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    numViewingSessions = db.Column(db.Integer, default=0)
    avgAnger = db.Column(db.Float, default=0)
    avgContempt = db.Column(db.Float, default=0)
    avgDisgust = db.Column(db.Float, default=0)
    avgFear = db.Column(db.Float, default=0)
    avgHappiness = db.Column(db.Float, default=0)
    avgNeutral = db.Column(db.Float, default=0)
    avgSadness = db.Column(db.Float, default=0)
    avgSuprise = db.Column(db.Float, default=0)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<' + self.__class__.__name__ + ': ' + self.name + '>'


class EmotionTimeFrame(db.Model):
    seconds = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'))
    film = db.relationship('Film', backref=db.backref('time_frames', lazy='dynamic'))
    anger = db.Column(db.Float)
    contempt = db.Column(db.Float)
    disgust = db.Column(db.Float)
    fear = db.Column(db.Float)
    happiness = db.Column(db.Float)
    neutral = db.Column(db.Float)
    sadness = db.Column(db.Float)
    suprise = db.Column(db.Float)

    def __repr__(self):
        return '<' + self.__class__.__name__ + ': ' + self.film.name + ' - ' + self.seconds + '>'
