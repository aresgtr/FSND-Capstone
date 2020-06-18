from sqlalchemy import Column, Integer, String, DateTime, ARRAY, Float
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# TODO: will be replaced by Heroku
database_path = 'postgresql://postgres:password@localhost:5432/capstone'

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Game(db.Model):
    __tablename__ = 'Game'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    developers = Column(ARRAY(String))
    publishers = Column(ARRAY(String))
    release_date = Column(DateTime())
    platforms = Column(ARRAY(String))
    review_score = Column(Float)
    genre = Column(ARRAY(String))
    transaction = db.relationship("Transaction", backref="Game", lazy='dynamic')

    def __init__(self, name, developers, publishers, release_date, platforms, review_score, genre):
        self.name = name
        self.developers = developers
        self.publishers = publishers
        self.release_date = release_date
        self.platforms = platforms
        self.review_score = review_score
        self.genre = genre

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'developers': self.developers,
            'publishers': self.publishers,
            'release_date': self.release_date,
            'platforms': self.platforms,
            'review_score': self.review_score,
            'genre': self.genre
        }


class Customer(db.Model):
    __tablename__ = 'Customer'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone = Column(String)
    country = Column(String)
    state = Column(String)
    transaction = db.relationship("Transaction", backref="Customer", lazy='dynamic')

    def __init__(self, first_name, last_name, email, phone, country, state):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.country = country
        self.state = state

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'country': self.country,
            'state': self.state
        }


class Transaction(db.Model):
    __tablename__ = 'Transaction'

    id = Column(Integer, primary_key=True)
    time_of_transaction = Column(DateTime())
    amount = Column(Float)
    review = Column(String)
    game_id = Column(Integer, db.ForeignKey('Game.id'), nullable=False)
    customer_id = Column(Integer, db.ForeignKey('Customer.id'), nullable=False)

    def __init__(self, time_of_transaction, amount, review, game, customer):
        self.time_of_transaction
        self.time_of_transaction = time_of_transaction
        self.amount = amount
        self.review = review
        self.Game = game
        self.Customer = customer

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'time_of_transaction': self.time_of_transaction,
            'amount': self.amount,
            'review': self.review,
            'game_id': self.game_id,
            'customer_id': self.customer_id
        }
