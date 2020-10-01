import unittest
from app.models import Post, User
from app import db


class PostModelTest(unittest.TestCase):
    def setUp(self):
        self.user_stude = User(username='stude', password='qwerty', email='test@test.com')
        self.new_post = Post(id=1, title='Test', content='This is a test post', user_id=self.user_stude.id)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.body, 'This git repository is under development')
        self.assertEquals(self.new_post.user_id, self.user_stude.id)

    def test_save_post(self):
        self.new_post.save()
        self.assertTrue(len(Post.query.all()) > 0)

    def test_get_post(self):
        self.new_post.save()
        got_post = Post.get_post(1)
        self.assertTrue(got_post is not None)



#class MyTestCase(unittest.TestCase):
    #def test_something(self):
        #self.assertEqual(True, False)