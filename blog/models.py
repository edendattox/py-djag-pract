from django.db import models
from django.utils.encoding import smart_text
from django.utils import timezone
from .validators import validate_author_email, validate_justin
# from django.db.models import Model

# Create your models here.


PUBLISH_CHOICES = (
    ('draft', 'Draft'),
    ('publish', 'Publish'),
    ('private', 'Private'),
)


class PostModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    active = models.BooleanField(default=True)  # null = True empty in the database
    title = models.CharField(max_length=226, verbose_name='Post title', unique=True)
    content = models.TextField(null=True, blank=True)
    publish = models.CharField(max_length=120, default='draft', choices=PUBLISH_CHOICES)
    view_count = models.IntegerField(default=0)
    publish_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    author_email = models.EmailField(max_length=240, validators=[validate_justin], null=True, blank=True)

    class Meat:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        # unique_together = [('title', 'slug')]

    def __unicode__(self):  # python 2 you can also do self.title
        return smart_text('something')

    def __str__(self):  # python 3 you can also do self.title
        return smart_text('something')


'''
python manage.py makemigrations #every time you change models.py
python manage.py migrate

ModelField


'''
