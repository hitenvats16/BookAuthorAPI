from django.db import models

from author.models import CustomUser

# Creating model for books


class Book(models.Model):
    id = models.AutoField
    title = models.CharField(default='', max_length=50)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    likes = models.ManyToManyField(CustomUser, related_name='book_like')
    no_of_likes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title
