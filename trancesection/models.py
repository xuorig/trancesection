from trancesection import db


class Podcast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    episodes = db.relationship('Episode', backref = 'podcast', lazy = 'dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Podcast %r>' % (self.name)

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(200))
    podcast_id = db.Column(db.Integer, db.ForeignKey('podcast.id'))
    trax = db.relationship('Track', backref = 'episode', lazy = 'dynamic')

    def __init__(self, number, podcast_id):
        self.number = number
        self.podcast_id = podcast_id

    def __repr__(self):
        return '<Episode %r>' % (self.number)


class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'))
    name = db.Column(db.String(50))
    youtube_url = db.Column(db.String(50))
    grooveshark_url = db.Column(db.String(50))
    soundcloud_url = db.Column(db.String(50))

    def __init__(self,name,episode_id):
        self.name = name
        self.episode_id = episode_id

    def __repr__(self):
        return '<Track %r>' % (self.name)
