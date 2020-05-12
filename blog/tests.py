from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user( # get_user_model is active user
            username='testuser', # here create a dummy username and password
            email='test@email.com',
            password='secret'
        )
        self.post = Post.objects.create(  # create a object in model
            title='A good title',
            body='Nice body content',
            author=self.user, # this one is foreign key of username
        )

    def test_string_representation(self): # check the dunder string which returns post title
        post = Post(title= 'A sample title')
        self.assertEqual(str(post), post.title) # check those 'a good title' and 'a sample title' both are string or not

    def test_get_absolute_url(self):
        self.assertEquals(self.post.get_absolute_url(), '/post/1/') # check absolute_url and create a url (post/1)

    def test_post_content(self):  # checking for post
        self.assertEqual(f'{self.post.title}', 'A good title') # f string represents a string and check using assertEaual
        self.assertEqual(f'{self.post.author}','testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home')) # client is a dummy web browser for simulating GET and POST,here take object who return home page
        self.assertEqual(response.status_code, 200) # confirm the homepage returns a 200 HTTP status code,it check the http request
        self.assertContains(response, 'Nice body content') # here check contains the body portion or not
        self.assertTemplateUsed(response, 'home.html') # in list view using home.html or not

    def test_post_detail_view(self):
        response = self.client.get('/post/1/') # response is the object who get this url
        no_response = self.client.get('/post/100000/') # this is not a vali url,so not a valid object
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404) # incorrect page returns 404
        self.assertContains(response, 'A good title') # check the post title,you can also check the post body
        self.assertTemplateUsed(response, 'post_detail.html') # check it returns this template or not

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'),{ # the template is post_new
            'title': 'New title',
            'body': 'New text',
            'author': self.user, # here creating a new title,body and author for testing
        })
        self.assertEqual(response.status_code, 200) # check for Http response
        self.assertContains(response, 'New title')  # check the new title is create in here or not(contains new title or body text or not)
        self.assertContains(response, 'New text')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args='1'),{  # in post update use post_edit template,here update(dummy) first post whose pk=1
            'title': 'Updated title',
            'body': 'Updated text', # here update the title and body and check this
        })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.get(
            reverse('post_delete', args='1') # if we delete (dummy) first post then confirm return Http(200) for success
        )
        self.assertEqual(response.status_code, 200)

