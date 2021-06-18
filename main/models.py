from django.db import models

# Create your models here.
class LibraryBooks(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=150)
    bid = models.CharField(max_length=50)
    date = models.CharField(max_length=12)
    duedate = models.CharField(max_length=12)
    def __str__(self):
        return self.bid
