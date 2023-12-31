# test_models.py
import unittest
from app import app, db
from app.models.user import User
from app.models.post import Post
from app.models.comment import Comment

class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_user_creation(self):
        user = User(username='testuser', email='testuser@example.com', password='testpassword')
        db.session.add(user)
        db.session.commit()

        retrieved_user = User.query.filter_by(username='testuser').first()

        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.username, 'testuser')

    def test_post_creation(self):
        user = User(username='testuser', email='testuser@example.com', password='testpassword')
        db.session.add(user)
        db.session.commit()

        post = Post(title='Test Post', content='This is a test post.', author=user)
        db.session.add(post)
        db.session.commit()

        retrieved_post = Post.query.filter_by(title='Test Post').first()

        self.assertIsNotNone(retrieved_post)
        self.assertEqual(retrieved_post.title, 'Test Post')
        self.assertEqual(retrieved_post.author, user)

    def test_comment_creation(self):
        user = User(username='testuser', email='testuser@example.com', password='testpassword')
        db.session.add(user)
        db.session.commit()

        post = Post(title='Test Post', content='This is a test post.', author=user)
        db.session.add(post)
        db.session.commit()

        comment = Comment(content='This is a test comment.', user=user, post=post)
        db.session.add(comment)
        db.session.commit()

        retrieved_comment = Comment.query.filter_by(content='This is a test comment.').first()

        self.assertIsNotNone(retrieved_comment)
        self.assertEqual(retrieved_comment.content, 'This is a test comment.')
        self.assertEqual(retrieved_comment.user, user)
        self.assertEqual(retrieved_comment.post, post)

    # ... other model-related tests

if __name__ == '__main__':
    unittest.main()
