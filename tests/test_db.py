# test_db.py
import unittest
from app import app, db
from app.models.user import User
from app.models.post import Post

class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_database_initialization(self):
        # Test if the database is properly initialized
        with app.app_context():
            self.assertIsNotNone(db)
            self.assertTrue(db.engine)

    def test_user_model(self):
        # Test if the User model is defined and can be used
        with app.app_context():
            user = User(username='testuser', email='test@example.com', password='testpassword')
            db.session.add(user)
            db.session.commit()

            retrieved_user = User.query.filter_by(username='testuser').first()
            self.assertIsNotNone(retrieved_user)
            self.assertEqual(retrieved_user.username, 'testuser')

    def test_post_model(self):
        # Test if the Post model is defined and can be used
        with app.app_context():
            user = User(username='testuser', email='test@example.com', password='testpassword')
            db.session.add(user)
            db.session.commit()

            post = Post(title='Test Post', content='This is a test post', author=user)
            db.session.add(post)
            db.session.commit()

            retrieved_post = Post.query.filter_by(title='Test Post').first()
            self.assertIsNotNone(retrieved_post)
            self.assertEqual(retrieved_post.title, 'Test Post')

if __name__ == '__main__':
    unittest.main()
