from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import Post


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='A good title',
            text='Nice body content',
            author=self.user,
        )

    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(str(self.post.title), 'A good title')
        self.assertEqual(str(self.post.author), 'testuser')
        self.assertEqual(str(self.post.text), 'Nice body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('viewblogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listblogs.html')
        self.assertContains(response, 'A good title')

    def test_post_detail_view(self):
        no_response = self.client.get('/blog/post/100000/')
        self.assertEqual(no_response.status_code, 404)

        response = self.client.get('/blog/post/1/')
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'post_detail.html')


