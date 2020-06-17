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

    return app


APP = create_app()

if __name__ == '__main__':
    # APP.run(host='0.0.0.0', port=8080, debug=True)
    APP.run()
