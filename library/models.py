from django.db import models

class Book(models.Model):
    title            = models.CharField(max_length=225)
    author           = models.CharField(max_length=225)
    isbn             = models.CharField(max_length=13, unique=True)
    published_date   = models.DateField()
    genre            = models.CharField(max_length=25)
    language         = models.CharField(max_length=50)
    total_copies     = models.IntegerField()
    available_copies = models.IntegerField(blank=True, null=True)
    status           = models.BooleanField(default=True)
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.title} by {self.author}'


