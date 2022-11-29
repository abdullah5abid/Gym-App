from django.db import models

CATEGORY = [
    ('20 minutes', ('20 minutes')),
    ('30 minutes', ('30 minutes')),
    ('45 minutes', ('45 minutes')),
    ('60 minutes', ('60 minutes')),
    ('75 minutes', ('75 minutes')),
    ('90 minutes', ('90 minutes'))
]

# Create your models here.
class Sessions(models.Model):
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=100, choices=CATEGORY)
    exercise1 = models.CharField(max_length=100)
    exercise2 = models.CharField(max_length=100)
    exercise3 = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Sessions"