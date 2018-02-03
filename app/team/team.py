from sqlalchemy.dialects.postgresql import JSON

from app import db


class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    players = db.Column(JSON)
    score = db.Column(db.Integer)
    wins = db.Column(db.Integer)
    loses = db.Column(db.Integer)
    draws = db.Column(db.Integer)
    logo = db.Column(db.String)

    def __init__(self, players,score,wins,loses,draws,logo):
        self.draws = draws
        self.logo = logo
        self.players = players
        self.score = score
        self.wins = wins
        self.loses = loses

    def __repr__(self):
        return '<id {}>'.format(self.id)