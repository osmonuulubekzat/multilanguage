from django.db import models


# Create your models here.
class Bloggers(models.Model):
    name = models.CharField(max_length=120, verbose_name="Blogger")
    text = models.TextField(verbose_name="text")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "this is a test"
        verbose_name_plural = "this is a test"
