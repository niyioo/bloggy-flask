# test_posts.py

import unittest
from app import create_app, db
from app.models import User, Post

class PostsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(testing=True)
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_create_post(self):
        # Create a test user
        user = User(username='testuser', email='test@example.com', password='testpassword')
        db.session.add(user)
        db.session.commit()

        # Login as the test user
        self.client.post('/login', data=dict(username='testuser', password='testpassword'))

        # Create a test post
        response = self.client.post('/create', data=dict(title='Test Post', content='This is a test post'))

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
        response = self.client.get(f'/{post.id}')

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
        self.client.post('/login', data=dict(username='testuser', password='testpassword'))

        # Create a test post
        post = Post(title='Test Post', content='This is a test post', author=user)
        db.session.add(post)
        db.session.commit()

        # Edit the test post
        response = self.client.post(f'/edit/{post.id}', data=dict(title='Updated Post', content='This post is updated'))

        # Check if the post is edited successfully (you may need to adjust this based on your actual implementation)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Post updated successfully!', response.data)

    def test_delete_post(self):
        # Create a test user
        user = User(username='testuser', email='test@example.com', password='testpassword')
        db.session.add(user)
        db.session.commit()

        # Login as the test user
        self.client.post('/login', data=dict(username='testuser', password='testpassword'))

        # Create a test post
        post = Post(title='Test Post', content='This is a test post', author=user)
        db.session.add(post)
        db.session.commit()

        # Delete the test post
        response = self.client.post(f'/delete/{post.id}')

        # Check if the post is deleted successfully (you may need to adjust this based on your actual implementation)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Post deleted successfully!', response.data)

if __name__ == '__main__':
    unittest.main()
