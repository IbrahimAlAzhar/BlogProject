from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        # reference is to build in user model that django provides for authentication
        'auth.User',  # django build in user is author in here,here author is foreign key of User
        on_delete=models.CASCADE, # many to one relationship each user has multiple post
    )
    body = models.TextField()

    def __str__(self):
        return self.title # for return the title of model

    def get_absolute_url(self): # when post update or create then it redirect to post detail url
        # sets canonical url for an object if the structure of your urls changes in the future the reference to the specific object is the same
        return reverse('post_detail', args=[str(self.id)]) # here return post_detail url after create form,post_detail needs pk which is id
        # reverse reference an object by url template name
