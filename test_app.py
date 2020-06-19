import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db

"""
Global Variables
"""
game_to_insert = {
    "name": "Halo 4",
    "developers": [
        "343 Industries"
    ],
    "publishers": [
        "Microsoft Game Studios"
    ],
    "release_date": "2012-11-06",
    "platforms": [
        "Xbox 360"
    ],
    "review_score": 9.8,
    "genre": [
        "Shooter"
    ]
}


class CapstoneTestCase(unittest.TestCase):
    """
    Tokens
    """

    manager = os.environ['MANAGER']
    sales = os.environ['SALES']

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = 'postgresql://postgres:password@localhost:5432/capstone_test'
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    Test cases
    """

    def test01_retrieve_games(self):
        res = self.client().get('/games')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['games']), 5)
        self.assertEqual(data['num_of_games'], 5)

    def test02_insert_game_sales(self):
        res = self.client().post('/games', headers={"Authorization": "Bearer {}".format(self.sales)}, json=game_to_insert)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'action not permitted or authentication fails')

    def test03_insert_game_manager(self):
        res = self.client().post('/games', headers={"Authorization": "Bearer {}".format(self.manager)}, json=game_to_insert)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['games']), 6)
        self.assertEqual(data['num_of_games'], 6)

    def test04_update_game_sales(self):
        body = {
            "name": "Halo Four",
            "genre": [
                "Shooter",
                "FPS"
            ]
        }

        res = self.client().patch('/games/6', headers={"Authorization": "Bearer {}".format(self.sales)}, json=body)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'action not permitted or authentication fails')

    def test05_update_game_manager(self):
        body = {
            "name": "Halo Four",
            "genre": [
                "Shooter",
                "FPS"
            ]
        }

        res = self.client().patch('/games/6', headers={"Authorization": "Bearer {}".format(self.manager)}, json=body)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['games'][5]['name'], 'Halo Four')

    def test06_delete_game_sales(self):
        res = self.client().delete('/games/6', headers={"Authorization": "Bearer {}".format(self.sales)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'action not permitted or authentication fails')

    def test07_delete_game_manager(self):
        res = self.client().delete('/games/6', headers={"Authorization": "Bearer {}".format(self.manager)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['games']), 5)
        self.assertEqual(data['num_of_games'], 5)

    def test08_404_delete_game_not_exist(self):
        res = self.client().delete('/games/999', headers={"Authorization": "Bearer {}".format(self.manager)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'not found')

    def test09_retrieve_customers_without_auth(self):
        res = self.client().get('/customers')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'action not permitted or authentication fails')

    def test10_retrieve_customers_sales(self):
        res = self.client().get('/customers', headers={"Authorization": "Bearer {}".format(self.sales)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['num_of_customers'], 3)
        self.assertEqual(len(data['customers']), 3)

    #
    def test11_retrieve_customers_manager(self):
        res = self.client().get('/customers', headers={"Authorization": "Bearer {}".format(self.manager)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['num_of_customers'], 3)
        self.assertEqual(len(data['customers']), 3)

    def test12_422_insert_customer_no_name(self):
        body = {
            "email": "123@example.com"
        }

        res = self.client().post('/customers', headers={"Authorization": "Bearer {}".format(self.manager)}, json=body)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'unprocessable')

    def test13_insert_customer(self):
        customer_to_insert = {
            "first_name": "Hello",
            "last_name": "World",
            "email": "helloworld@example.com",
            "phone": "00000000",
            "country": "Mars",
            "state": "A part of Mars"
        }

        res = self.client().post('/customers', headers={"Authorization": "Bearer {}".format(self.manager)}, json=customer_to_insert)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['num_of_customers'], 4)
        self.assertEqual(len(data['customers']), 4)

    def test14_update_customer(self):
        body = {
            "first_name": "Hi",
            "country": "This is Mars"
        }

        res = self.client().patch('/customers/4', headers={"Authorization": "Bearer {}".format(self.manager)}, json=body)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['customers'][3]['country'], 'This is Mars')

    def test15_404_update_customer_not_exist(self):
        body = {
            "first_name": "Hi",
            "country": "This is Mars"
        }

        res = self.client().patch('/customers/999', headers={"Authorization": "Bearer {}".format(self.manager)}, json=body)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'not found')

    def test16_delete_customer(self):
        res = self.client().delete('/customers/4', headers={"Authorization": "Bearer {}".format(self.manager)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['customers']), 3)
        self.assertEqual(data['num_of_customers'], 3)

    def test17_delete_customer_not_exist(self):
        res = self.client().delete('/customers/999', headers={"Authorization": "Bearer {}".format(self.manager)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'not found')

    def test18_retrieve_transactions_sales(self):
        res = self.client().get('/transactions', headers={"Authorization": "Bearer {}".format(self.sales)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'action not permitted or authentication fails')

    def test19_retrieve_transactions_manager(self):
        res = self.client().get('/transactions', headers={"Authorization": "Bearer {}".format(self.manager)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['transactions']), 3)
        self.assertEqual(data['num_of_transactions'], 3)

    def test20_insert_transaction(self):
        transaction = {
            "time_of_transaction": "2020-06-18",
            "amount": 19.99,
            "game_id": 5,
            "customer_id": 3
        }

        res = self.client().post('/transactions', headers={"Authorization": "Bearer {}".format(self.manager)}, json=transaction)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['transactions']), 4)
        self.assertEqual(data['num_of_transactions'], 4)

    def test21_422_insert_transaciton_wrong_game_id(self):
        transaction = {
            "time_of_transaction": "2020-06-18",
            "amount": 19.99,
            "game_id": 999,
            "customer_id": 3
        }

        res = self.client().post('/transactions', headers={"Authorization": "Bearer {}".format(self.manager)}, json=transaction)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'unprocessable')


if __name__ == '__main__':
    unittest.main()
