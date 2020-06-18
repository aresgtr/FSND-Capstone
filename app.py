from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import setup_db, Game, Customer, Transaction
from auth.auth import AuthError, requires_auth


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
    @requires_auth('post:games')
    def insert_game(payload):
        print(payload)

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
    @requires_auth('patch:games')
    def update_game(payload, id):
        print(payload)

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
    @requires_auth('delete:games')
    def delete_game(payload, id):
        print(payload)

        game = Game.query.filter(Game.id == id).one_or_none()

        if game is None:
            abort(404)

        try:
            game.delete()

            return retrieve_games()

        except:
            abort(422)

    @app.route('/customers')
    @requires_auth('get:customers')
    def retrieve_customers(payload):
        print(payload)

        customer_query = Customer.query.order_by(Customer.id).all()

        customers = [customer.format() for customer in customer_query]

        return jsonify({
            'success': True,
            'customers': customers,
            'num_of_customers': len(customer_query)
        })

    @app.route('/customers', methods=['POST'])
    @requires_auth('post:customers')
    def insert_customer(payload):
        print(payload)

        body = request.get_json()

        first_name = body.get('first_name', None)
        last_name = body.get('last_name', None)

        if (first_name is None) or (last_name is None):
            abort(422)

        email = body.get('email', None)
        phone = body.get('phone', None)
        country = body.get('country', None)
        state = body.get('state', None)

        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            country=country,
            state=state)

        try:
            customer.insert()

            return retrieve_customers()

        except:
            abort(422)

    @app.route('/customers/<int:id>', methods=['PATCH'])
    @requires_auth('patch:customers')
    def update_customer(payload, id):
        print(payload)

        customer = Customer.query.filter(Customer.id == id).one_or_none()

        if customer is None:
            abort(404)

        body = request.get_json()
        first_name = body.get('first_name', None)
        last_name = body.get('last_name', None)
        email = body.get('email', None)
        phone = body.get('phone', None)
        country = body.get('country', None)
        state = body.get('state', None)

        if first_name:
            customer.first_name = first_name

        if last_name:
            customer.last_name = last_name

        if email:
            customer.email = email

        if phone:
            customer.phone = phone

        if country:
            customer.country = country

        if state:
            customer.state = state

        customer.update()
        return retrieve_customers()

    @app.route('/customers/<int:id>', methods=['DELETE'])
    @requires_auth('delete:customers')
    def delete_customer(payload, id):
        print(payload)

        customer = Customer.query.filter(Customer.id == id).one_or_none()

        if customer is None:
            abort(404)

        try:
            customer.delete()

            return retrieve_customers()

        except:
            abort(422)

    @app.route('/transactions')
    @requires_auth('get:transactions')
    def retrieve_transactions(payload):
        print(payload)

        transaction_query = Transaction.query.order_by(Transaction.id).all()

        transactions = [transaction.format() for transaction in transaction_query]

        return jsonify({
            'success': True,
            'transactions': transactions,
            'num_of_transactions': len(transaction_query)
        })

    @app.route('/transactions', methods=['POST'])
    @requires_auth('post:transactions')
    def insert_transaction(payload):
        print(payload)

        body = request.get_json()

        time = body.get('time_of_transaction', None)
        amount = body.get('amount', None)
        game_id = body.get('game_id', None)
        customer_id = body.get('customer_id', None)

        if (time is None) or (amount is None) or (game_id is None) or (customer_id is None):
            abort(422)

        review = body.get('review', None)

        game = Game.query.filter(Game.id == game_id).one_or_none()
        customer = Customer.query.filter(Customer.id == customer_id).one_or_none()

        if (game is None) or (customer is None):
            abort(422)

        transaction = Transaction(
            time_of_transaction=time,
            amount=amount,
            review=review,
            game=game,
            customer=customer)

        try:
            transaction.insert()

            return retrieve_transactions()

        except:
            abort(422)

    # Error Handling

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error"
        }), 500

    @app.errorhandler(AuthError)
    def auth_error(AuthError):
        return jsonify({
            "success": False,
            "error": AuthError.status_code,
            'message': 'action not permitted or authentication fails'
        }), AuthError.status_code

    return app


APP = create_app()

if __name__ == '__main__':
    # APP.run(host='0.0.0.0', port=8080, debug=True)
    APP.run()
