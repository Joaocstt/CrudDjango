from pyexpat import model
from turtle import update
from django.db import models

class Task(models.Model):
    STATUS = (
        ('Fazendo', 'Fazendo'),
        ('Feito', 'Feito')
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(
        max_length=10,
        choices=STATUS,
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.title