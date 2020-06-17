import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Game, Customer, Transaction


# TODO: paginate

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/games')
    def retrieve_games():
        game_query = Game.query.order_by(Game.id).all()

        games = [game.format() for game in game_query]

        return jsonify({
            'success': True,
            'games': games,
            'num_of_games': len(game_query)
        })

    @app.route('/games', methods=['POST'])
    def insert_game():
        body = request.get_json()

        name = body.get('name', None)

        if name is None:
            abort(422)

        developers = body.get('developers', None)
        publishers = body.get('publishers', None)
        release_date = body.get('release_date', None)
        platforms = body.get('platforms', None)
        review_score = body.get('review_score', None)
        genre = body.get('genre', None)

        game = Game(
            name=name,
            developers=developers,
            publishers=publishers,
            release_date=release_date,
            platforms=platforms,
            review_score=review_score,
            genre=genre)

        try:
            game.insert()

            return retrieve_games()

        except:
            abort(422)

    @app.route('/games/<int:id>', methods=['PATCH'])
    def update_game(id):
        game = Game.query.filter(Game.id == id).one_or_none()

        if game is None:
            abort(404)

        body = request.get_json()
        name = body.get('name', None)
        developers = body.get('developers', None)
        publishers = body.get('publishers', None)
        release_date = body.get('release_date', None)
        platforms = body.get('platforms', None)
        review_score = body.get('review_score', None)
        genre = body.get('genre', None)

        if name:
            game.name = name

        if developers:
            game.developers = developers

        if publishers:
            game.publishers = publishers

        if release_date:
            game.release_date = release_date

        if platforms:
            game.platforms = platforms

        if review_score:
            game.review_score = review_score

        if genre:
            game.genre = genre

        game.update()
        return retrieve_games()

    @app.route('/games/<int:id>', methods=['DELETE'])
    def delete_game(id):
        game = Game.query.filter(Game.id == id).one_or_none()

        if game is None:
            abort(404)

        try:
            game.delete()

            return retrieve_games()

        except:
            abort(422)

    @app.route('/customers')
    def retrieve_customers():
        customer_query = Customer.query.order_by(Customer.id).all()

        customers = [customer.format() for customer in customer_query]

        return jsonify({
            'success': True,
            'customers': customers,
            'num_of_customers': len(customer_query)
        })

    return app


APP = create_app()

if __name__ == '__main__':
    # APP.run(host='0.0.0.0', port=8080, debug=True)
    APP.run()
