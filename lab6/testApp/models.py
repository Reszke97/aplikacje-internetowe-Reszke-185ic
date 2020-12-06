from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Moje-książki"

    def __str__(self):
        return self.title


"""
class Test(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField

    class Meta:
        verbose_name_plural = "odwiedziny"

    def __str__(self):
        return self.title
"""
