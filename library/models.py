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


class Member(models.Model):
    full_name  = models.CharField(max_length=255)
    email      = models.EmailField(blank=True, null=True, unique=True)
    phone      = models.CharField(max_length=15, blank=True, null=True, unique=True)
    address    = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.full_name} - Phone: {self.phone}'