from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        # reference is to build in user model that django provides for authentication
        'auth.User',  # django build in user is author in here,here author is foreign key of User
        on_delete=models.CASCADE, # many to one relationship each user has multiple post
    )
    body = models.TextField()

    def __str__(self):
        return self.title
