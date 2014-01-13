from trancesection import db


class Podcast(db.Model):
    __tablename__ = 'podcasts'
    id = db.Column('podcast_id', db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    episodes = db.relationship('Episode', backref = 'podcast', lazy = 'dynamic')

    def __repr__(self):
        return '<Podcast %r>' % (self.name)

class Episode(db.Model):
    __tablename__ = 'episodes'
    id = db.Column('episode_id', db.Integer, primary_key=True)
    number = db.Column(db.String(200))
    podcast_id = db.Column(db.Integer, db.ForeignKey('Podcast.podcast_id'))
    trax = db.relationship('Track', backref = 'episode', lazy = 'dynamic')

    def __repr__(self):
        return '<Episode %r>' % (self.number)


class Track(db.Model):
    __tablename__ = 'tracks'
    id = db.Column('track_id', db.Integer, primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('Episode.episode_id'))
    name = db.Column(db.String(50))
    youtube_url = db.Column(db.String(50))
    grooveshark_url = db.Column(db.String(50))
    soundcloud_url = db.Column(db.String(50))

    def __repr__(self):
        return '<Track %r>' % (self.name)
