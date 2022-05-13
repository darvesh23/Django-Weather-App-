from django.db import models

class City(models.Model):
    DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'