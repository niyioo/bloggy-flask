# test_auth.py

import unittest
from app import app, db
from app.models.user import User

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app(testing=True)
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_user_registration(self):
        response = self.client.post('/register', data=dict(
            username='testuser',
            email='testuser@example.com',
            password='testpassword',
        ), follow_redirects=True)

        user = User.query.filter_by(username='testuser').first()

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'testuser')

    def test_user_login(self):
        # Assuming you have a registered user from the registration test
        user = User(username='testuser', email='testuser@example.com', password='testpassword')
        db.session.add(user)
        db.session.commit()

        response = self.client.post('/login', data=dict(
            username='testuser',
            password='testpassword',
        ), follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        # Add assertions for successful login

    # ... other authentication-related tests


if __name__ == '__main__':
    unittest.main()
