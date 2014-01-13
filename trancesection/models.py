from trancesection import db


class Podcast(db.Model):
    __tablename__ = 'podcasts'
    id = db.Column('podcast_id', db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    trax = db.relationship('Track', backref = 'podcast', lazy = 'dynamic')

    def __repr__(self):
        return '<Podcast %r>' % (self.name)

class Track(db.Model):
    __tablename__ = 'tracks'
    id = db.Column('track_id', db.Integer, primary_key=True)
    podcast_id = db.Column(db.Integer, db.ForeignKey('podcasts.podcast_id'))
    name = db.Column(db.String(50))
    youtube_url = db.Column(db.String(50))
    grooveshark_url = db.Column(db.String(50))
    soundcloud_url = db.Column(db.String(50))

    def __repr__(self):
        return '<Track %r>' % (self.name)
