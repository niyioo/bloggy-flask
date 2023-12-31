# test_posts.py
import unittest
from app import app, db
from app.models.user import User
from app.models.post import Post

class PostsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_create_post(self):
        # Create a test user
        user = User(username='testuser', email='test@example.com', password='testpassword')
        db.session.add(user)
        db.session.commit()

        # Login as the test user
        self.app.post('/login', data=dict(username='testuser', password='testpassword'))

        # Create a test post
        response = self.app.post('/create', data=dict(title='Test Post', content='This is a test post'))

        # Check if the post is created successfully (you may need to adjust this based on your actual implementation)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Post created successfully!', response.data)

    def test_view_post(self):
        # Create a test user
        user = User(username='testuser', email='test@example.com', password='testpassword')
        db.session.add(user)
        db.session.commit()

        # Create a test post
        post = Post(title='Test Post', content='This is a test post', author=user)
        db.session.add(post)
        db.session.commit()

        # View the test post
        response = self.app.get(f'/{post.id}')

        # Check if the post is displayed (you may need to adjust this based on your actual implementation)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Post', response.data)
        self.assertIn(b'This is a test post', response.data)

    def test_edit_post(self):
        # Create a test user
        user = User(username='testuser', email='test@example.com', password='testpassword')
        db.session.add(user)
        db.session.commit()

        # Login as the test user
        self.app.post('/login', data=dict(username='testuser', password='testpassword'))

        # Create a test post
        post = Post(title='Test Post', content='This is a test post', author=user)
        db.session.add(post)
        db.session.commit()

        # Edit the test post
        response = self.app.post(f'/edit/{post.id}', data=dict(title='Updated Post', content='This post is updated'))

        # Check if the post is edited successfully (you may need to adjust this based on your actual implementation)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Post updated successfully!', response.data)

    def test_delete_post(self):
        # Create a test user
        user = User(username='testuser', email='test@example.com', password='testpassword')
        db.session.add(user)
        db.session.commit()

        # Login as the test user
        self.app.post('/login', data=dict(username='testuser', password='testpassword'))

        # Create a test post
        post = Post(title='Test Post', content='This is a test post', author=user)
        db.session.add(post)
        db.session.commit()

        # Delete the test post
        response = self.app.post(f'/delete/{post.id}')

        # Check if the post is deleted successfully (you may need to adjust this based on your actual implementation)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Post deleted successfully!', response.data)

if __name__ == '__main__':
    unittest.main()
