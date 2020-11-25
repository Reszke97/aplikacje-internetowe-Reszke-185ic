from django.db import models
from django.utils import timezone


class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tytul = models.CharField(max_length=200)
    tekst = models.TextField()
    data_utworzenia = models.DateTimeField(
            default=timezone.now)
    data_opublikowania = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.data_opublikowania = timezone.now()
        self.save()

    def __str__(self):
        return self.tytul
