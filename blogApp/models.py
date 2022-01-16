from django.db import models
from datetime import *

# Models
class Blog(models.Model):
    user = models.CharField('user', max_length=50)
    title = models.CharField('title', max_length=50)

    def __str__(self):
        return f'{self.user}: {self.title}'


class Author(models.Model):
    user = models.CharField('user', max_length=50)
    name = models.CharField('name', max_length=50)
    date_subscription = models.DateField('date_subscription', auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.name}: {self.user}'
    

class Article(models.Model):
    title = models.CharField('title', max_length=50)
    text_article = models.CharField('text_article', max_length=1000)
    topic = models.CharField('topic', max_length=50)
    date_creation = models.DateField('date_creation', auto_now=False, auto_now_add=False, default=datetime.now)

    def __str__(self):
        return f'{self.title}: {self.topic}'



    


