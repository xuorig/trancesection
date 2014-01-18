from trancesection import db
import re


class Podcast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    imgurl = db.Column(db.String(500))
    episodes = db.relationship('Episode', backref = 'podcast', lazy = 'dynamic')
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __init__(self, name, imgurl):
        self.name = name
        self.imgurl = imgurl
        self.slug = slugify(name)

    def __repr__(self):
        return '<Podcast %r>' % (self.name)

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(200))
    podcast_id = db.Column(db.Integer, db.ForeignKey('podcast.id'))
    trax = db.relationship('Track', backref = 'episode', lazy = 'dynamic')
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __init__(self, number, podcast_id):
        self.number = number
        self.podcast_id = podcast_id

    def __repr__(self):
        return '<Episode %r>' % (self.number)


class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'))
    name = db.Column(db.String(50))
    slug = db.Column(db.String(200))
    youtube_url = db.Column(db.String(50))
    grooveshark_url = db.Column(db.String(50))
    soundcloud_url = db.Column(db.String(50))
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __init__(self,name,episode_id):
        self.name = name
        self.episode_id = episode_id
        self.slug = slugify(name)

    def __repr__(self):
        return '<Track %r>' % (self.name)


_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')


def slugify(text, delim=u'-'):
    """Generates an ASCII-only slug."""
    result = []
    for word in _punct_re.split(text.lower()):
        word = word.encode('translit/long')
        if word:
            result.append(word)
    return unicode(delim.join(result))