import datetime
from django.db import models
from django.utils import timezone

#Models go here

class Author(models.Model):
    name        = models.CharField      (max_length = 50)
    joined      = models.DateTimeField  ( 'date joined' )
    job_title   = models.CharField      (max_length = 50)
    def __str__(self):
        return self.name

class Post(models.Model):
    title       = models.CharField      (max_length = 100)
    content     = models.TextField      (max_length = 5000)
    pub_date    = models.DateTimeField  ('date published')
    tags        = models.CharField      (max_length = 300)
    author      = models.ForeignKey     (Author, on_delete = models.CASCADE)
    def __str__(self):
        return self.title
